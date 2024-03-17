from pydantic import BaseModel, EmailStr
from annotated_types import MinLen, MaxLen
from typing import Annotated

class CreateUser(BaseModel):
    # username: Field(str, min_length=3, max_length=20) это старый способ но тоже рабочий
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr