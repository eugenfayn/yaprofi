from pydantic import BaseModel
from typing import List


class Participant(BaseModel):
    id: int # идентификатор участника
    name: str # идентификатор группы
    wish: str | None # пожелание участника
    group_id: int
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
        
class CreateGroup(BaseModel):
    name: str # название группы
    description: str | None # описание группы

class CreateGroupResponse(BaseModel):
    id: int # идентификатор группы

class CreateParticipant(BaseModel):
    name: str # идентификатор группы
    wish: str | None # пожелание участника
    recipient: int | None# айдишник того, кому будут дарить подарок

class LessParticipant(BaseModel):
    id: int
    name: str
    wish: str| None

class ParticipantToss(BaseModel):
    id: int
    name: str
    wish: str | None
    recipient: LessParticipant

class Toss(BaseModel):
    participants: List[ParticipantToss]