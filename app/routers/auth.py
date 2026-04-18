from fastapi import APIRouter

router = APIRouter()

@router.post("/signup")
def signup():
    return {"message": "signup - todo"}

@router.post("/login")
def login():
    return {"message": "login - todo"}