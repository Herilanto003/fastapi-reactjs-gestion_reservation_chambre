from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from services.models import Customers, Bookings
from services.schemas import CustomerSchema
from datetime import datetime


def create_new_customer(req: CustomerSchema, db: Session):
    if req.nom == '':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'status': 'error', 'error_type': req.nom})
    if req.cin == '':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'status': 'error', 'error_type': req.cin})
    if req.telephone == '':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'status': 'error', 'error_type': req.telephone})
    if req.email == '':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'status': 'error', 'error_type': req.email})
        
    new_customer = Customers(
        nom=req.nom,
        prenoms=req.prenoms,
        cin=req.cin,
        telephone=req.telephone,
        email=req.email
    )
    
    
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    
    
    return new_customer


def get_all_customers(db: Session):
    all_customers = db.query(Customers).all()
    
    return all_customers


def get_one_customers(id: int, db: Session):
    customer_select = db.query(Customers).filter(Customers.id_customer==id)
    
    if not customer_select.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'not found'})
    
    return customer_select.first()


def update_one_customer(req: CustomerSchema, id: int, db: Session):
    customer_select = db.query(Customers).filter(Customers.id_customer==id)
    
    if not customer_select.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'not found'})
    
    customer_select.update({
        'nom': req.nom,
        'prenoms': req.prenoms,
        'cin': req.cin,
        'telephone': req.telephone,
        'email': req.email,
        'updated_at': datetime.now()
    })
    
    db.commit()
    
    return {
        'detail': {
            'success': True
        }
    }
    

def delete_one_customer(id: int, db: Session):
    customer_select = db.query(Customers).filter(Customers.id_customer==id) 
    booking_select = db.query(Bookings).filter(Bookings._id_customer==id)
    
    if not customer_select.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'not found'})
    
    booking_select.delete(synchronize_session=False)    
    customer_select.delete(synchronize_session=False)
    
    db.commit()
    
    return {
        'detail': {
            'success': True
        }
    }
    
    
    