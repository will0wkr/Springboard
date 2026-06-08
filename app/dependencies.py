from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.config import settings
from supabase import create_client

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials  # Bearer 자동 제거, 토큰만 추출

    try:
        res = supabase.auth.get_user(token)
        return res.user
    except Exception:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰입니다")