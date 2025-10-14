from utils.utils import encriptar_contrasena, validar_contrasena
from repositorios.repositorio_usuario import RepositorioUsuario
from models.usuario import Usuario


class ServicioAutenticacion:
    def __init__(self):
        self.user_repo = RepositorioUsuario()

    def iniciar_sesion(self, email, password):
        fila = self.user_repo.obtener_por_email(email)
        if not fila:
            return None
        id_usuario, nombre, email_usuario, hash_pass, rol = fila
        if encriptar_contrasena(password) == hash_pass:
            return Usuario(id_usuario, nombre, email_usuario, rol, hash_pass)
        return None

    def cambiar_contrasena(self, id_usuario, pass_actual, pass_nueva):
        fila = self.user_repo.obtener_por_id(id_usuario)
        if not fila:
            return False
        _, _, _, hash_actual, _ = fila
        if encriptar_contrasena(pass_actual) != hash_actual:
            return False
        if not validar_contrasena(pass_nueva):
            return False
        hash_nuevo = encriptar_contrasena(pass_nueva)
        return self.user_repo.actualizar_contrasena(id_usuario, hash_nuevo)

    def cambiar_nombre(self, id_usuario, nombre_nuevo):
        return self.user_repo.actualizar_nombre(id_usuario, nombre_nuevo)
