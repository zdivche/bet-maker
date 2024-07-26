from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.schemas import BetCreate, Bet
from app.core.usecases.bets import BetUseCase
from app.infrastucture.database import get_db
from app.infrastucture.repositories.bets import BetRepository

router = APIRouter()

@router.post("/bets", response_model=Bet)
async def create_bet(bet: BetCreate, db: AsyncSession = Depends(get_db)):
    repository = BetRepository(db)
    use_case = BetUseCase(repository)
    return await use_case.create_bet(bet)

@router.get("/bets", response_model=List[Bet])
async def get_bets(db: AsyncSession = Depends(get_db)):
    repository = BetRepository(db)
    use_case = BetUseCase(repository)
    return await use_case.get_bets()