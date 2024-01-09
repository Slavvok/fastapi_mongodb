from datetime import datetime
from typing import Annotated, Optional

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

PyObjectId = Annotated[str, BeforeValidator(str)]


class RandomNumber(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    number: float = Field(...)
    date: datetime = Field(default=datetime.now())
    user_id: str = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "number": 3.1
            }
        }
    )
