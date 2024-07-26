from pydantic import BaseModel
from enum import Enum

class BetStatusEnum(str, Enum):
    PENDING = "ещё не сыграла"
    WON = "выиграла"
    LOST = "проиграла"

class BetCreate(BaseModel):
    event_id: str
    amount: float

class Bet(BaseModel):
    id: str
    event_id: str
    amount: float
    status: BetStatusEnum
    class Config:
        from_attributes = True