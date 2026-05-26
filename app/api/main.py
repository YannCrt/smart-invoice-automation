from fastapi import FastAPI, UploadFile, File
import shutil
import os

from app.services.pdf_service import extract_invoice_data
from app.database.db import SessionLocal
from app.models.invoice import Invoice

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload/")
async def upload_invoice(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # extraction
    data = extract_invoice_data(file_path)

    # DB
    db = SessionLocal()

    invoice = Invoice(
        supplier=data["supplier"],
        invoice_number=data["invoice_number"],
        date=data["date"],
        amount=data["amount"],
        vat=data["vat"],
        status="Processed"
    )

    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    return {
        "message": "Invoice processed",
        "data": data
    }