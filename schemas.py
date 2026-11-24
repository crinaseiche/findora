from pydantic import BaseModel, Field


class ExtractionRequest(BaseModel):
    text: str = Field(min_length=1)


class ExtractionResponse(BaseModel):
    technologies: list[str] = Field(
        description="Technologies explicitly mentioned in the text."
    )

    locations: list[str] = Field(
        description="Geographical locations explicitly mentioned in the text. "
        "Exclude work arrangements such as remote, hybrid or on-site."
    )

    summary: str = Field(description="A concise factual summary of the provided text.")
