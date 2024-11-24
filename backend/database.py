import uuid

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, select, func

from .config import config

database_path = "sqlite+aiosqlite:///valentine.db"

# Настройка базы данных
engine = create_async_engine(database_path, echo=config.DEBUG)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

# Определение модели
class Valentine(Base):
    __tablename__ = "valentine"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True, index=True, default=lambda: str(uuid.uuid4()))
    recipient = Column(String, index=True)
    message = Column(String)
    

# Функции CRUD для Valentine
async def create_valentine(db: AsyncSession, recipient: str, message: str):
    valentine = Valentine(recipient=recipient, message=message)
    db.add(valentine)
    await db.commit()
    await db.refresh(valentine)
    return valentine

async def get_valentine(valentine_uuid: int):
    async with SessionLocal() as db:
        result = await db.execute(select(Valentine).filter(Valentine.uuid == valentine_uuid))
        return result.scalars().first()

async def get_total_valentine_id_count():
    async with SessionLocal() as db:
        result = await db.execute(select(func.count(Valentine.id)))
        return result.scalar()

# Создание таблицы
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)