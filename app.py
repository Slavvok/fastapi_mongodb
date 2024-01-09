from fastapi import FastAPI

from routes.auth import router as auth_router
from routes.number import router as number_router

app = FastAPI()


app.include_router(auth_router, tags=["Auth"])
app.include_router(number_router, tags=["Numbers"], prefix="/number")
