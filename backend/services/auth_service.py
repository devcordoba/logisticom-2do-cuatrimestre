from typing import Optional
from utils.utils import encriptar_contrasena, validar_contrasena
from repositories.user_repository import UserRepository


class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def login(self, email: str, password: str):
        row = self.user_repo.get_by_email(email)
        if not row:
            return None
        user_id, nombre, email_usuario, pass_hash, rol = row
        if encriptar_contrasena(password) == pass_hash:
            # Return a simple dict for user representation to avoid circular deps
            return {"id_usuario": user_id, "nombre": nombre, "email": email_usuario, "rol": rol, "password": pass_hash}
        return None

    def change_password(self, user_id: int, current_password: str, new_password: str) -> bool:
        row = self.user_repo.get_by_id(user_id)
        if not row:
            return False
        _, _, _, current_hash, _ = row
        if encriptar_contrasena(current_password) != current_hash:
            return False
        if not validar_contrasena(new_password):
            return False
        new_hash = encriptar_contrasena(new_password)
        return self.user_repo.update_password(user_id, new_hash)

    def change_name(self, user_id: int, new_name: str) -> bool:
        return self.user_repo.update_name(user_id, new_name)
