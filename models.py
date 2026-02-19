import os

from dotenv import load_dotenv
from sqlalchemy import Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import (Mapped, declarative_base, mapped_column,
                            sessionmaker)

load_dotenv()

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DSN = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
engine = create_engine(DSN)
Base = declarative_base()
Session = sessionmaker(bind=engine)


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


class Request(Base):
    __tablename__ = "requests"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    from_currency: Mapped[str] = mapped_column(String(3))


class Response(Base):
    __tablename__ = "responses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    into_currency: Mapped[str] = mapped_column(String(3))
    currency_value: Mapped[int] = mapped_column(Float)
    request: Mapped[int] = mapped_column(Integer, ForeignKey("requests.id", ondelete="CASCADE"))
