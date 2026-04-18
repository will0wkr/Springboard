from fastapi import FastAPI
from app.routers import auth, posts

app = FastAPI(title="소나기 게시판")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])

@app.get("/")
def health_check():
    return {"status": "ok", "message": "소나기 게시판 서버 실행 중"}