from fastapi import FastAPI
from services.database_config import engine
from services.models import Base
from routers.customerRouter import router as customer_router
from routers.roomRouter import router as room_router
from routers.bookingRouter import router as booking_router
from routers.userRouter import router as user_router
from routers.dataRouter import router as data_router
from fastapi.middleware.cors import CORSMiddleware


# Création de la base de données
Base.metadata.create_all(engine)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/home')
def home():
    return {
        "message": "welcome to server"
    }


app.include_router(user_router)
app.include_router(booking_router)
app.include_router(room_router)
app.include_router(customer_router)
app.include_router(data_router)