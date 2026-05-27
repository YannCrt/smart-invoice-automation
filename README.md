# Smart Invoice Automation

Professional mini-platform for automated invoice processing using Python, FastAPI, Streamlit and workflow automation.

---

## Features

- PDF invoice upload
- Automatic invoice data extraction
- SQLite database storage
- Interactive dashboard
- Invoice history tracking
- Workflow automation via webhook
- Professional modular architecture

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Frontend | Streamlit |
| Database | SQLite |
| PDF Parsing | pdfplumber |
| Data Processing | pandas |
| Automation | Webhooks / Power Automate simulation |
| Version Control | Git & GitHub |

---

## Project Architecture

smart-invoice-automation/

├── app/
│ ├── api/
│ ├── services/
│ ├── models/
│ ├── database/
│ └── utils/
│
├── frontend/
├── uploads/
├── tests/
├── screenshots/
├── README.md
└── requirements.txt

---

## Workflow

1. User uploads a PDF invoice
2. FastAPI backend processes the file
3. PDF text extraction with pdfplumber
4. Regex-based invoice parsing
5. Data storage in SQLite
6. Dashboard visualization in Streamlit
7. Automation webhook triggered

---

## Installation

### Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-invoice-automation.git
cd smart-invoice-automation

