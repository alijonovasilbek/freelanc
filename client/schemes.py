from pydantic import BaseModel
from datetime import datetime, time




class GigPost(BaseModel):
    gigs_title: str
    price: float
    duration: int
    description: str


class Gig(BaseModel):
    id: int
    gigs_title: str
    duration: int
    price: float
    description: str
    user_id: int


class GigCategoryPost(BaseModel):
    category_name: str
    gigs_id: int


class GigSkillPost(BaseModel):
    skill_name: str
    gigs_id: int


class GigFilePost(BaseModel):
    file_url: str
    gigs_id: int


class GigCategory(BaseModel):
    id:int
    category_name: str
    gigs_id: int    