from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.schemas import EventUpdate
from app.core.usecases.events import EventUseCase
from app.infrastucture.database import get_db
from app.infrastucture.repositories.bets import BetRepository

router = APIRouter()

@router.put("/events/{event_id}")
async def update_event(event_id: str, event: EventUpdate, db: AsyncSession = Depends(get_db)):
    repository = BetRepository(db)
    use_case = EventUseCase(repository)
    await use_case.update_event_status(event_id, event.status)
    return {"message": "Event status updated successfully"}