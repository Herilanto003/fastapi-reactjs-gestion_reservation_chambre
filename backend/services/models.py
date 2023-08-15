from sqlalchemy import Integer, String, Boolean, ForeignKey, Column, DateTime, func, Enum, Date
from sqlalchemy.orm import relationship
from services.database_config import Base
from enum import Enum as PyEnum


# enum class for booking state
class BookingState(PyEnum):
    free = 'free'   
    pending = 'pending'
    occupied = 'occupied' 


# customers classes
class Customers(Base):
    __tablename__ = 'customers'
    
    id_customer = Column(Integer, primary_key=True, nullable=False)
    nom = Column(String, nullable=False)
    prenoms = Column(String, nullable=True)
    cin = Column(String, nullable=False)
    telephone = Column(String, nullable=False)
    email = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())
    
    booking = relationship('Bookings', back_populates='customer')
    
    
# rooms class
class Rooms(Base):
    __tablename__ = 'rooms'
    
    id_room = Column(Integer, primary_key=True, nullable=False)
    number = Column(String, nullable=False)
    price_day = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())
    
    booking = relationship('Bookings', back_populates='room')
    

# booking class  
class Bookings(Base):
    __tablename__ = 'bookings'
    
    id_booking = Column(Integer, primary_key=True, nullable=False)
    date = Column(Date, nullable=False)
    day_number = Column(Integer, nullable=False)
    is_paid = Column(Boolean, nullable=False, default=False) 
    _id_customer = Column(Integer, ForeignKey('customers.id_customer'), nullable=False)
    _id_room = Column(Integer, ForeignKey('rooms.id_room'), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())
    
    customer = relationship('Customers', back_populates='booking')
    room = relationship('Rooms', back_populates='booking')
    
    
# user class
class Users(Base):
    __tablename__ = 'users'
    
    id_user = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, default='ROLE_USER') 
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())