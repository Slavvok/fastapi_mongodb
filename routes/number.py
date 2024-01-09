from fastapi import APIRouter, Depends, HTTPException, status

from connector import db
from models.number import RandomNumber
from models.user import User
from routes.auth import get_current_user

router = APIRouter()


@router.get("/")
async def get_number(number: int | float, current_user: User = Depends(get_current_user)):
    try:
        number_collection = db.get_collection("numbers")
        number = await number_collection.find_one({"user_id": current_user.id, "number": number}, {'_id': False})
        if not number:
            raise HTTPException(
                status_code=status.HTTP_204_NO_CONTENT,
                detail="No such record found.",
            )
        return {"number": number["number"]}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad request",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.post("/")
async def add_number(number, current_user: User = Depends(get_current_user)):
    try:
        number_collection = db.get_collection("numbers")
        number_in_db = RandomNumber(
            number=number,
            user_id=current_user.id,
        ).model_dump()
        await number_collection.insert_one(number_in_db)
        return {"number": number}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad request",
            headers={"WWW-Authenticate": "Bearer"},
        )


# @router.patch("/number")
# async def update_number():
#     try:
#         number_id = 1
#         return RandomNumber(number=number_id).model_dump()
#     except:
#         raise HTTPException(400)
