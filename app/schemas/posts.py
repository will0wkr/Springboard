from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional


class PostCreate(BaseModel):
    title: str
    content: str


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class PostResponse(BaseModel):
    id: UUID
    title: str
    content: str
    author_id: UUID
    created_at: datetime
    updated_at: datetime