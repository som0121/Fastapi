from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from typing import Annotated

class PostBase(BaseModel):
    title:str
    content: str
    published:bool = True

class Postcreate(PostBase):
    pass

class userout(BaseModel):
    id: int
    email:EmailStr
    created_at : datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    id:int
    created_at : datetime
    owner_id: int

    owner: userout

    class Config:
        orm_mode = True


class usercreate(BaseModel):
    
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email:EmailStr
    password: str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id: int
    email: str | None = None 

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(le=1)]

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True