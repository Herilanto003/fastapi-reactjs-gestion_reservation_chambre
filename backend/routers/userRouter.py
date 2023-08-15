from fastapi import APIRouter, HTTPException, Depends, status
from services.authentication.utils import get_hashed_password, create_access_token, create_refresh_token, verify_password
from services.schemas import UserSchema, UserSchemaView
from services.models import Users
from sqlalchemy.orm import Session
from services.database_config import get_db
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from passlib.context import CryptContext


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


router = APIRouter(
    prefix='/api/user',
    tags=['API USERS']
)


@router.post('/signup')
def create_user(req: UserSchema, db: Session = Depends(get_db)):
    # check first if user already existed
    all_email = []
    user_existed = db.query(Users).all()
    
    for value in user_existed:
        all_email.append(value.email)
        
    if req.email in all_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': 'email'})
    
    new_user = Users(
        email=req.email,
        password=get_hashed_password(req.password),
        role=req.role
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        'detail': {'success': True}
    }
    

@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):    
    user = db.query(Users).filter(Users.email==form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="email_not_found"
        )
    
    hashed_pass = user.password
    
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='password_error'
        )
        
    user_token = {
        'email': user.email,
        'id': user.id_user,
        'role': user.role
    }
    
    return {
        "users": user_token,
        "access_token": create_access_token(user_token),
        "refresh_token": create_refresh_token(user_token),
    }