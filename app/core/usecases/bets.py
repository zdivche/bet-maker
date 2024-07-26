from app.core.schemas import BetCreate, Bet
from app.infrastucture.repositories.bets import BetRepository

class BetUseCase:
    def __init__(self, repository: BetRepository):
        self.repository = repository

    async def create_bet(self, bet: BetCreate) -> Bet:
        return await self.repository.create_bet(bet.event_id, bet.amount)

    async def get_bets(self):
        return await self.repository.get_bets()