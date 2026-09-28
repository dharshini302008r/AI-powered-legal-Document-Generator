from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Document(BaseModel):
    document_type: str
    details: str

@app.get("/")
def home():
    return {"message": "LegalEase is running"}

@app.post("/generate")
def generate(data: Document):

    document = f"""
LEGAL DOCUMENT

Document Type:
{data.document_type}

Details:
{data.details}
"""

    return {"document": document}