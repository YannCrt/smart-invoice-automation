import pdfplumber
import re

def extract_invoice_data(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    supplier = "Unknown"

    amount_match = re.search(r"(\d+[\.,]\d{2})", text)
    amount = float(amount_match.group(1).replace(",", ".")) if amount_match else 0.0

    vat_match = re.search(r"TVA\s*:?\s*(\d+[\.,]\d{2})", text)
    vat = float(vat_match.group(1).replace(",", ".")) if vat_match else 0.0

    invoice_match = re.search(r"(?:Invoice|Facture)\s*#?\s*([A-Z0-9\-]+)", text, re.IGNORECASE)
    invoice_number = invoice_match.group(1) if invoice_match else "N/A"

    date_match = re.search(r"(\d{2}/\d{2}/\d{4})", text)
    date = date_match.group(1) if date_match else "N/A"

    return {
        "supplier": supplier,
        "invoice_number": invoice_number,
        "date": date,
        "amount": amount,
        "vat": vat
    }