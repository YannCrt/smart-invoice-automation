from sqlalchemy import Column, Integer, String, Float
from app.database.db import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    supplier = Column(String)
    invoice_number = Column(String)
    date = Column(String)
    amount = Column(Float)
    vat = Column(Float)
    status = Column(String, default="Processed")