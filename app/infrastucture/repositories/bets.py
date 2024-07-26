from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from app.core.models import Bet as BetModel
from app.core.schemas import BetCreate, BetStatusEnum
import uuid
from typing import List

class BetRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_bet(self, event_id: str, amount: float) -> BetModel:
        bet_id = str(uuid.uuid4())
        bet = BetModel(id=bet_id, event_id=event_id, amount=amount, status=BetStatusEnum.PENDING)
        self.db.add(bet)
        await self.db.commit()
        await self.db.refresh(bet)
        return bet

    async def get_bets(self) -> List[BetModel]:
        result = await self.db.execute(select(BetModel))
        return result.scalars().all()

    async def update_event_status(self, event_id: str, status: str):
        result = await self.db.execute(select(BetModel).where(BetModel.event_id == event_id))
        bets = result.scalars().all()
        for bet in bets:
            bet.status = status
        await self.db.commit()