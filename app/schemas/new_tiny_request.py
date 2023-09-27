from pydantic import BaseModel, Field


class NewTinyRequest(BaseModel):
    name: str = Field(min_length=3, max_length=100)