from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from services.models import Bookings, Rooms, Customers
from services.schemas import BookingSchema
from datetime import datetime, timedelta
import json


def create_new_booking(req: BookingSchema, db: Session):  
    all_id_room_occupied = [] 
    room_occupied = db.query(Rooms).filter(Rooms.id_room==req.id_room)
    new_s = req.date
    new_e = req.date + timedelta(days=req.day_number)
    if not room_occupied.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'room not found', 'error': 'room'})
    
    
    for value in room_occupied:
        all_id_room_occupied.append(value.id_room)

    
    if req.id_room in all_id_room_occupied:
        all_book = db.query(Bookings).filter(Bookings._id_room==req.id_room).all()
        for val in all_book:
            old_s = val.date
            old_e = val.date + timedelta(days=val.day_number)
            if (new_s >= old_s and new_s <= old_e) or (new_e <= old_e and new_e >= old_s ) or (new_s <= old_s and new_e >= old_e):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'room busy', 'error': 'room_busy'})

             
    new_booking = Bookings(
        _id_customer=req.id_customer,
        _id_room=req.id_room,
        date=req.date,
        is_paid=req.is_paid,
        day_number=req.day_number
    )
    
     
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    
    
    return new_booking


def get_all_bookings(db: Session):
    all_bookings = db.query(Bookings).all()
    
    return all_bookings


def get_one_bookings(id: int, db: Session):
    booking_select = db.query(Bookings).filter(Bookings.id_booking==id)
    
    if not booking_select.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'not found'})
    
    return booking_select.first()


def update_one_booking(req: BookingSchema, id: int, db: Session):
    booking_select = db.query(Bookings).filter(Bookings.id_booking==id)
    booking_update = db.query(Bookings).filter(Bookings.id_booking!=id).all()
    all_id_update = []
    
    for value in booking_update:
        all_id_update.append(value._id_room)    
    
    
    all_id_room_occupied = [] 
    room_occupied = db.query(Rooms).filter(Rooms.id_room==req.id_room)
    new_s = req.date
    new_e = req.date + timedelta(days=req.day_number)
    if not room_occupied.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'room not found', 'error': 'room'})
    
    
    for value in room_occupied:
        all_id_room_occupied.append(value.id_room)

    
    if req.id_room in all_id_update:
        all_book = db.query(Bookings).filter(Bookings._id_room==req.id_room and Bookings.id_booking!=id).all()
        for val in booking_update:
            old_s = val.date
            old_e = val.date + timedelta(days=val.day_number)
            if (new_s >= old_s and new_s <= old_e) or (new_e <= old_e and new_e >= old_s ) or (new_s <= old_s and new_e >= old_e):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'room busy', 'error': 'room_busy'})
    
    
    booking_select.update({
        '_id_room': req.id_room,
        '_id_customer': req.id_customer,
        'date': req.date,
        'day_number': req.day_number,
        'is_paid': req.is_paid,
        'updated_at': datetime.now()
    })
    
    db.commit()
    
    return {
        'detail': {
            'success': True
        }
    }
    

def delete_one_booking(id: int, db: Session):
    booking_select = db.query(Bookings).filter(Bookings.id_booking==id)
    
    if not booking_select.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'not found'})
    
    booking_select.delete(synchronize_session=False)
    
    db.commit()
    
    return {
        'detail': {
            'success': True
        }
    }
    
    
    
def get_all_bookings_calendar(db: Session):
    allData = []
    for b, r, c in db.query(Bookings, Rooms, Customers).filter(Bookings._id_room == Rooms.id_room).filter(Bookings._id_customer==Customers.id_customer).all():
        print(b.id_booking, b.date + timedelta(days=4), b.day_number)
        allData.append(
            {
                'title': f'Room number {b._id_room} is ocupied by {c.nom} {c.prenoms}',
                'start': b.date,
                'end': b.date + timedelta(days=b.day_number)
            }
        )
        
    return allData