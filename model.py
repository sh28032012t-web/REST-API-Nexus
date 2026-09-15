from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    first_name: str = Field(min_length=1, max_length=64)
    last_name: str = Field(min_length=1, max_length=64)
    age: int = Field(ge=0, le=150)

class UserUpdate(BaseModel):
    first_name: str = Field(min_length=1, max_length=64)
    last_name: str = Field(min_length=1, max_length=64)
    age: int = Field(ge=0, le=150)

class UserPatch(BaseModel):
    first_name: str | None = Field(min_length=1, max_length=64, default=None)
    last_name: str | None = Field(min_length=1, max_length=64, default=None)
    age: int | None = Field(ge=0, le=150, default=None)