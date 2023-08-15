from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.database_config import get_db
from services.authentication.deps import get_current_user
from services.models import Users, Bookings, Rooms, Customers
from sqlalchemy import func


router = APIRouter(
    prefix="/api/data",
    tags=["API DATA COLLECTION"]
)

@router.get('/data/collection/free-room')
def free_room(user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    all_rooms = db.query(Rooms).all()
    all_customers = db.query(Customers).all()
    all_bookings = db.query(Bookings).all()
    all_rooms_ocupied = db.query(Rooms).join(Bookings).filter(Bookings._id_room==Rooms.id_room).all()
    
    return {
        "rooms": len(all_rooms),
        "customers": len(all_customers),
        "bookings": len(all_bookings),
        "rooms_ocupied": len(all_rooms_ocupied)        
    }


@router.get('/data/collection/ocupied-room')
def ocupied_room(user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return 'ocupied room'


@router.get('/data/collection/money')
def money(user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return 'money'


@router.get('/data/collection/customer-money')
def customer_money(user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    allData = []
    for b, r in db.query(Customers, func.sum(Bookings.day_number*Rooms.price_day)).group_by().filter(Bookings._id_room == Rooms.id_room).filter(Bookings._id_customer==Customers.id_customer).group_by(Customers.id_customer).all():
        print(r, b.nom)
        allData.append({
            'cutomer': f'{b.nom} {b.prenoms}',
            'tarif': r
        })
    return allData