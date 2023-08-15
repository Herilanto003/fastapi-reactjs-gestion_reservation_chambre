from fastapi import APIRouter, HTTPException, status, Depends
from services.schemas import CustomerSchema, CustomerSchemaView
from sqlalchemy.orm import Session
from services.database_config import get_db
from api.customerApi import create_new_customer, get_all_customers, get_one_customers, update_one_customer, delete_one_customer
from typing import List
from services.authentication.deps import get_current_user
from services.models import Users


router = APIRouter(
    prefix="/api/customer",
    tags=["API CUSTOMERS"]
)


# router for creating a new customer
@router.post('/new', status_code=status.HTTP_201_CREATED)
def new_customer(req: CustomerSchema, user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return create_new_customer(req, db)


# router for gettin all customers
@router.get('/all')
def all_customers(user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_all_customers(db)


# router for getting just one customer
@router.get('/{id}')
def one_customer(id: int, user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_one_customers(id, db)


# router for updating just one customer
@router.put('/edit/{id}')
def update_customer(req: CustomerSchema, id: int, user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return update_one_customer(req, id, db)


# router for deleting one customer
@router.delete('/delete/{id}')
def delete_customer(id: int, user: Users = Depends(get_current_user), db: Session = Depends(get_db)):
    return delete_one_customer(id, db)