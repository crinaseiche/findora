from fastapi import FastAPI

from extraction_service import ExtractionService
from schemas import ExtractionRequest, ExtractionResponse

app = FastAPI(title="Findora API")

service = ExtractionService()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/v1/extractions", response_model=ExtractionResponse)
def extract_information(request: ExtractionRequest):
    return service.extract(request.text)
