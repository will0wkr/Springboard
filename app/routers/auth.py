from fastapi import APIRouter, HTTPException
from app.schemas.auth import SignupRequest, LoginRequest
from app.core.config import settings
from supabase import create_client

router = APIRouter()
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)

@router.post("/signup")
def signup(body: SignupRequest):
    try:
        res = supabase.auth.sign_up({
            "email": body.email,
            "password": body.password
        })
        return {"message": "회원가입 성공", "user": res.user.email}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(body: LoginRequest):
    try:
        res = supabase.auth.sign_in_with_password({
            "email": body.email,
            "password": body.password
        })
        return {
            "access_token": res.session.access_token,
            "token_type": "bearer"
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 틀렸습니다")