from typing import List, Optional, Tuple
from utils.utils import encriptar_contrasena, validar_contrasena
from repositories.user_repository import UserRepository
from repositories.role_repository import RoleRepository
from repositories.commission_repository import CommissionRepository


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.role_repo = RoleRepository()
        self.commission_repo = CommissionRepository()

    def find_user_by_email(self, email: str) -> Optional[Tuple]:
        return self.user_repo.get_by_email(email)

    def register_user(self, nombre: str, email: str, rol: str, password: str) -> bool:
        if self.user_repo.email_exists(email):
            return False
        id_rol = self.role_repo.get_id_by_name(rol)
        if id_rol is None:
            return False
        if not validar_contrasena(password):
            return False
        pass_hash = encriptar_contrasena(password)
        return self.user_repo.insert_user(nombre, email, pass_hash, id_rol)

    def list_users(self) -> List[Tuple]:
        return self.user_repo.list_all_with_roles()

    def change_role(self, user_id: int, rol_nuevo: str) -> bool:
        id_rol = self.role_repo.get_id_by_name(rol_nuevo)
        if id_rol is None:
            return False
        return self.user_repo.update_role(user_id, id_rol)

    def delete_user(self, user_id: int) -> bool:
        # Prevent deleting users with commissions
        if self.commission_repo.has_commissions_for_user(user_id):
            return False
        return self.user_repo.delete_user(user_id)
