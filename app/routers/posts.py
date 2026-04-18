from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_posts():
    return {"message": "게시글 목록 - todo"}

@router.post("/")
def create_post():
    return {"message": "게시글 작성 - todo"}

@router.get("/{post_id}")
def get_post(post_id: int):
    return {"message": f"게시글 {post_id} 조회 - todo"}

@router.put("/{post_id}")
def update_post(post_id: int):
    return {"message": f"게시글 {post_id} 수정 - todo"}

@router.delete("/{post_id}")
def delete_post(post_id: int):
    return {"message": f"게시글 {post_id} 삭제 - todo"}