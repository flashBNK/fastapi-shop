from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine( # соединение с бд
    settings.database_url,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # "фабрика для создания сессий"
Base = declarative_base()

def get_db():
    db = SessionLocal() # инициализация
    try:
        yield db # попытка передать сервису возможность поработать с бд
    finally:
        db.close() # закрытие бд

def init_db():
    Base.metadata.create_all(bind=engine) # инициализация бд с помощью engine