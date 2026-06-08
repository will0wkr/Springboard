from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.routers import auth, posts

app = FastAPI(title="소나기 게시판")

# ── 라우터 등록 ──
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])

# ── Static 파일 서빙 ──
# /static/index.html, /static/login.html, /static/post.html 접근 가능
app.mount("/static", StaticFiles(directory="static"), name="static")

# ── 루트 → 게시판으로 리다이렉트 ──
@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")
