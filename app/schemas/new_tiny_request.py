from pydantic import BaseModel, Field


class NewTinyRequest(BaseModel):
    url: str = Field(min_length=3, max_length=100)
