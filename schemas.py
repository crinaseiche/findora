
from pydantic import BaseModel, Field


class ExtractionRequest(BaseModel):
    text: str = Field(min_length=1)


class ExtractionResponse(BaseModel):
    technologies: list[str]
    locations: list[str]
    summary: str
