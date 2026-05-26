from app.database.db import engine, Base
from app.models.invoice import Invoice

Base.metadata.create_all(bind=engine)

print('Database created successfully.')