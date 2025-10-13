from typing import List, Tuple
from repositories.commission_repository import CommissionRepository


class CommissionService:
    def __init__(self):
        self.repo = CommissionRepository()

    def create_commission(self, user_id: int, descripcion: str) -> bool:
        return self.repo.insert(user_id, descripcion)

    def list_user_commissions(self, user_id: int) -> List[Tuple]:
        return self.repo.list_by_user_id(user_id)

    def list_all_commissions(self) -> List[Tuple]:
        return self.repo.list_all_with_user()

    def dispatch_commission(self, commission_id: int) -> bool:
        state = self.repo.get_state_by_id(commission_id)
        if state is None:
            return False
        if state == 'Despachado':
            return False
        return self.repo.mark_dispatched(commission_id)
