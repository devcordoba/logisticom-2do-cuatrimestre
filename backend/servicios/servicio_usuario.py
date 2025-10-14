from utils.utils import encriptar_contrasena, validar_contrasena
from repositorios.repositorio_usuario import RepositorioUsuario
from repositorios.repositorio_rol import RepositorioRol
from repositorios.repositorio_comision import RepositorioComision

class ServicioUsuario:
    def __init__(self):
        self.user_repo = RepositorioUsuario()
        self.rol_repo = RepositorioRol()
        self.comision_repo = RepositorioComision()

    def encontrar_usuario_por_email(self, email):
        return self.user_repo.obtener_por_email(email)

    def registrar_usuario(self, nombre, email, rol, password):
        if self.user_repo.existe_email(email):
            return False
        id_rol = self.rol_repo.obtener_id_por_nombre(rol)
        if id_rol is None:
            return False
        if not validar_contrasena(password):
            return False
        hash_pass = encriptar_contrasena(password)
        return self.user_repo.insertar_usuario(nombre, email, hash_pass, id_rol)

    def listar_todos(self):
        return self.user_repo.listar_todos_con_roles()

    def cambiar_rol(self, id_usuario, rol_nuevo):
        id_rol = self.rol_repo.obtener_id_por_nombre(rol_nuevo)
        if id_rol is None:
            return False
        return self.user_repo.actualizar_rol(id_usuario, id_rol)

    def eliminar_usuario(self, id_usuario):
        if self.comision_repo.tiene_comisiones_de_usuario(id_usuario):
            return False
        return self.user_repo.eliminar_usuario(id_usuario)
