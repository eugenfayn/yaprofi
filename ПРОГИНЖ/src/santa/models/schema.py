from pydantic import BaseModel
from typing import List


class Participant(BaseModel):
    id: int # идентификатор участника
    name: str # идентификатор группы
    wish: str # пожелание участника
    recipient: int | None# айдишник того, кому будут дарить подарок
    
class Group(BaseModel):
    id: int # идентификатор группы
    name: str # название группы
    description: str | None # описание группы

    class Config:
        orm_mode = True

class FullGroup(BaseModel):
    id: int # идентификатор группы
    name: str # название группы
    description: str | None # описание группы
    participants: List['Participant'] | None

    class Config:
        orm_mode = True
        


# post/group
class CreateGroup(BaseModel):
    name: str # название группы
    description: str | None # описание группы

class CreateGroupResponse(BaseModel):
    id: int # идентификатор группы


# get/group/{id}