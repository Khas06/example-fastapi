from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime
from .database import Base



class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str





class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse
    
    class Config:
        orm_mode = True


class PostVoteResponse(BaseModel):
    Post: PostResponse
    votes: int 

    class Config:
        orm_mode = True

        


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


class VoteCreate(Vote):
    pass


class VoteResponse(Vote):
    
    class Config:
        orm_mode = True




class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
