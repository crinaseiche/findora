import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from schemas import ExtractionResponse

load_dotenv()


class ExtractionService:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=os.environ["GEMINI_MODEL"],
            google_api_key=os.environ["GEMINI_API_KEY"],
            timeout=30,
            max_retries=0,
        )

        self.extractor = self.llm.with_structured_output(ExtractionResponse)

    def extract(self, text: str) -> ExtractionResponse:
        print("FINDORA: Starting Gemini request", flush=True)

        result = self.extractor.invoke(
            "Extract technologies, locations, and a short summary "
            "from the following text. "
            "Only extract information supported by the text:\n\n"
            f"{text}"
        )

        print("FINDORA: Gemini response received", flush=True)

        return result
