from fastapi import APIRouter, HTTPException, status, Depends
from services.schemas import BookingSchema, BookingSchemaView, BookingView
from sqlalchemy.orm import Session
from services.database_config import get_db
from api.bookingApi import create_new_booking, get_all_bookings, get_one_bookings, update_one_booking, delete_one_booking, get_all_bookings_calendar
from services.authentication.deps import get_current_user
from services.models import Users
from typing import List


router = APIRouter(
    prefix="/api/booking",
    tags=["API BOOKINGS"]
)


# router for creating a new customer
@router.post('/new', status_code=status.HTTP_201_CREATED)
def new_booking(req: BookingSchema, user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return create_new_booking(req, db)


# router for gettin all bookings
@router.get('/all')
def all_bookings(user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_all_bookings(db)

# router for gettin all bookings
@router.get('/calendar')
def calendar_bookings(user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_all_bookings_calendar(db)


# router for getting just one booking
@router.get('/{id}')
def one_booking(id: int, user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_one_bookings(id, db)


# router for updating just one booking
@router.put('/edit/{id}')
def update_booking(req: BookingSchema, id: int, user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return update_one_booking(req, id, db)


# router for deleting one booking
@router.delete('/delete/{id}')
def delete_booking(id: int, user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return delete_one_booking(id, db)