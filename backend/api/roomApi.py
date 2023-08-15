from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from services.models import Rooms, Bookings
from services.schemas import RoomSchema
from datetime import datetime


def create_new_room(req: RoomSchema, db: Session):
        
    new_room = Rooms(
        number=req.number,
        price_day=req.price_day,
        capacity=req.capacity
    )
    
    
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    
    
    return new_room


def get_all_rooms(db: Session):
    all_rooms = db.query(Rooms).all()
    
    return all_rooms


def get_one_room(id: int, db: Session):
    room_select = db.query(Rooms).filter(Rooms.id_room==id)
    
    if not room_select.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'not found'})
    
    return room_select.first()


def update_one_room(req: RoomSchema, id: int, db: Session):
    room_select = db.query(Rooms).filter(Rooms.id_room==id)
    
    if not room_select.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'not found'})
    
    room_select.update({
        'number': req.number,
        'price_day': req.price_day,
        'capacity': req.capacity,
        'updated_at': datetime.now()
    })
    
    db.commit()
    
    return {
        'detail': {
            'success': True
        }
    }
    

def delete_one_room(id: int, db: Session):
    room_select = db.query(Rooms).filter(Rooms.id_room==id)
    booking_select = db.query(Bookings).filter(Bookings._id_room==id)
    
    if not room_select.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'not found'})
    
    booking_select.delete(synchronize_session=False)   
    room_select.delete(synchronize_session=False)
    
    db.commit()
    
    return {
        'detail': {
            'success': True
        }
    }
    
    
    