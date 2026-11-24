from fastapi import FastAPI, HTTPException
from langchain_google_genai.chat_models import GoogleAPIError

from extraction_service import ExtractionService
from schemas import ExtractionRequest, ExtractionResponse

app = FastAPI(title="Findora API")

service = ExtractionService()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/v1/extractions", response_model=ExtractionResponse)
def extract_information(request: ExtractionRequest):
    try:
        return service.extract(request.text)
    except GoogleAPIError as exc:
        raise HTTPException(
            status_code=503, detail="AI provider is temporarily unavailable."
        ) from exc
