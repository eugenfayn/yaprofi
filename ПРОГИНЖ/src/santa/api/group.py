from fastapi import APIRouter
from models.schema import FullGroup,Group,CreateGroup,CreateGroupResponse
from typing import List
from fastapi import Depends
from db import get_session,Session
import tables
router = APIRouter(prefix='/group')

@router.get('/{id}',response_model=FullGroup)
def get_group(id:int,session:Session = Depends(get_session)):
    s = session.query(tables.Group).filter(tables.Group.id==id).first()
    return s

@router.get('s/',response_model=List[Group])
def get_groups(session:Session = Depends(get_session)):
    groups = session.query(tables.Group).all()
    return groups

@router.post('/',response_model=Group)
def create_group(group:CreateGroup,session:Session = Depends(get_session)):
    new_group = tables.Group(name=group.name,description=group.description)
    session.add(new_group)
    session.commit()
    session.refresh(new_group)
    return new_group

@router.delete('/{id}')
def delete_group(id:int,session:Session = Depends(get_session)):
    s = session.query(tables.Group).filter(tables.Group.id==id).first()
    if s:
        session.delete(s)
        session.commit()
        return "Deleted"
    return "Нет такой группы"

@router.put('/{id}',response_model=Group)
def change_group(id:int,group:CreateGroup,session:Session = Depends(get_session)):
    gr = session.query(tables.Group).filter(tables.Group.id==id).first()
    
    eturn 0