from typing import Annotated, Optional

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

PyObjectId = Annotated[str, BeforeValidator(str)]


class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "username": "user1",
                "email": "test@test.test",
                "full_name": "Test User",
                "disabled": None,
            }
        }
    )


class UserInDB(User):
    hashed_password: str
