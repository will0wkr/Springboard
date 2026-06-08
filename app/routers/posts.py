from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_current_user
from app.schemas.posts import PostCreate, PostUpdate, PostResponse
from app.core.config import settings
from supabase import create_client

router = APIRouter()
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_ROLE_KEY)


@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return {"email": user.email, "id": str(user.id)}


@router.get("/")
def get_posts():
    res = supabase.table("posts").select("*").order("created_at", desc=True).execute()
    return res.data


@router.post("/", response_model=PostResponse)
def create_post(body: PostCreate, user=Depends(get_current_user)):
    res = supabase.table("posts").insert({
        "title": body.title,
        "content": body.content,
        "author_id": str(user.id)
    }).execute()

    if not res.data:
        raise HTTPException(status_code=400, detail="게시글 작성 실패")

    return res.data[0]


@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: str):
    res = supabase.table("posts").select("*").eq("id", post_id).execute()

    if not res.data:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다")

    return res.data[0]


@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id: str, body: PostUpdate, user=Depends(get_current_user)):
    # 게시글 존재 여부 확인
    res = supabase.table("posts").select("*").eq("id", post_id).execute()

    if not res.data:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다")

    post = res.data[0]

    # 작성자 본인 확인
    if post["author_id"] != str(user.id):
        raise HTTPException(status_code=403, detail="수정 권한이 없습니다")

    # 전달된 필드만 업데이트 (None 제외)
    update_data = body.model_dump(exclude_none=True)

    if not update_data:
        raise HTTPException(status_code=400, detail="수정할 내용이 없습니다")

    res = supabase.table("posts").update(update_data).eq("id", post_id).execute()

    if not res.data:
        raise HTTPException(status_code=400, detail="게시글 수정 실패")

    return res.data[0]


@router.delete("/{post_id}")
def delete_post(post_id: str, user=Depends(get_current_user)):
    # 게시글 존재 여부 확인
    res = supabase.table("posts").select("*").eq("id", post_id).execute()

    if not res.data:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다")

    post = res.data[0]

    # 작성자 본인 확인
    if post["author_id"] != str(user.id):
        raise HTTPException(status_code=403, detail="삭제 권한이 없습니다")

    supabase.table("posts").delete().eq("id", post_id).execute()

    return {"message": "게시글이 삭제되었습니다"}