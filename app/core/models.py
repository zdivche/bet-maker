from sqlalchemy import Column, String, Float, Enum
from sqlalchemy.ext.declarative import declarative_base
from app.core.schemas import BetStatusEnum

Base = declarative_base()

class Bet(Base):
    __tablename__ = "bets"

    id = Column(String, primary_key=True, index=True)
    event_id = Column(String, index=True)
    amount = Column(Float, nullable=False)
    status = Column(Enum(BetStatusEnum), default=BetStatusEnum.PENDING)