from fastapi import APIRouter, HTTPException, status, Depends
from services.schemas import RoomSchema, RoomSchemaView
from sqlalchemy.orm import Session
from services.database_config import get_db
from api.roomApi import create_new_room, get_all_rooms, get_one_room, update_one_room, delete_one_room
from typing import List
from services.authentication.deps import get_current_user
from services.models import Users


router = APIRouter(
    prefix="/api/room",
    tags=["API ROOMS"]
)


# router for creating a new room
@router.post('/new', status_code=status.HTTP_201_CREATED)
def new_room(req: RoomSchema, user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return create_new_room(req, db)


# router for getting all rooms
@router.get('/all')
def all_rooms(user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_all_rooms(db)


# router for getting just one room
@router.get('/{id}')
def one_room(id: int, user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_one_room(id, db)


# router for updating just one room
@router.put('/edit/{id}')
def update_room(req: RoomSchema, id: int, user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return update_one_room(req, id, db)


# router for deleting one room
@router.delete('/delete/{id}')
def delete_room(id: int, user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return delete_one_room(id, db)