# app/models.py
import os

sqlite_file_name = os.getenv("SQLITE_PATH", "babybot.db")  # default to local

from sqlmodel import SQLModel, Field, create_engine

class Baby(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    ageInMonths: int
    notes: str | None = None

# SQLite DB file
sqlite_file_name = "babybot.db"
engine = create_engine(f"sqlite:///{sqlite_file_name}", echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
