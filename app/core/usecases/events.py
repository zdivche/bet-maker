
from app.infrastucture.repositories.bets import BetRepository


class EventUseCase:
    def __init__(self, repository: BetRepository):
        self.repository = repository

    async def update_event_status(self, event_id: str, status: str):
        await self.repository.update_event_status(event_id, status)