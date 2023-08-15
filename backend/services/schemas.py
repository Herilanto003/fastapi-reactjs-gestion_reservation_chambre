from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date, timedelta
from services.models import BookingState



# schema for create or update of customers
class CustomerSchema(BaseModel):
    nom: str
    prenoms: str
    cin: str
    telephone: str
    email: str
    
    class Config:
        orm_mode=True
    

# schema for customers display
class CustomerSchemaView(CustomerSchema):
    created_at: datetime
    updated_at: datetime
    id_customer: int
    
    class Config:
        from_attributs = True
        

# schema for create or update of rooms
class RoomSchema(BaseModel):
    number: str
    price_day: int
    capacity: int
    
    class Config():
        orm_mode = True
    

# schema for customers display
class RoomSchemaView(RoomSchema):
    created_at: datetime
    updated_at: datetime
    id_room: int
    
    class Config:
        from_attributs = True
        
        
# schema for create or update of booking
class BookingSchema(BaseModel):
    date: date
    day_number: int
    id_customer: int
    id_room: int
    is_paid: bool
    

# schema for customers display
class BookingSchemaView(BookingSchema):
    created_at: datetime
    updated_at: datetime
    id_booking: int
    
    class Config:
        from_attributs = True
        

class BookingView(BaseModel):
    date: date
    day_number: int
    _id_customer: int
    _id_room: int
    is_paid: bool
    created_at: datetime
    updated_at: datetime
    id_booking: int
    customer: Optional[CustomerSchema]
    room: Optional[RoomSchema]
    
    
    class Config:
        orm_mode=True
        
# schema for create or update of user
class UserSchema(BaseModel):
    email: str 
    password: str
    role: str
    

# schema for customers display
class UserSchemaView(UserSchema):
    created_at: datetime
    updated_at: datetime
    id_user: int
    
    class Config:
        from_attributs = True
        
# schema pour creer un user
class UserSchema(BaseModel):
    nom: str
    prenoms: Optional[str]
    email: str
    password: str
    

# schema pour token
class UserToken(BaseModel):
    id_user: int
    email: str
    role: str
    
    class Config:
        from_attributs = True
        orm_mode=True


# schema pour login user
class UserLogin(BaseModel):
    email: str
    password: str
    
    class Config:
        orm_mode = True
