from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://pspslari:011125@localhost:5432/clinicadb"

# preciso criar a engine
engine = create_engine(DATABASE_URL, echo=False)

# criar a sessão
SessionLocal = sessionmaker(bind=engine, autoflush=False)

# base dos models
Base = declarative_base()
