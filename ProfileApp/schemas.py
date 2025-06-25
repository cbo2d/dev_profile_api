from pydantic import BaseModel
from typing import List


class SkillOut(BaseModel):
    name: str
    class Config:
        orm_mode = True


class ProjectOut(BaseModel):
    title: str
    description: str
    technologies: List[str]
    link: str
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
