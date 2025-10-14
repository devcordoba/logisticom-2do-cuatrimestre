from models.usuario import Usuario
from utils.utils import encriptar_contrasena
from servicios.servicio_autenticacion import ServicioAutenticacion
from servicios.servicio_usuario import ServicioUsuario

class Login:
    def __init__(self):
        self.usuario_actual = None
        self.password_hash = None
        self.autenticacion = ServicioAutenticacion()
        self.servicio_usuario = ServicioUsuario()

    def inicio_de_sesion(self, email, password):
        usuario = self.autenticacion.iniciar_sesion(email, password)
        if not usuario:
            return False
        self.usuario_actual = usuario
        self.password_hash = usuario.password
        return True

    def cambiar_pass(self, pass_actual, pass_nueva):
        if not self.usuario_actual:
            return False
        ok = self.autenticacion.cambiar_contrasena(self.usuario_actual.id_usuario, pass_actual, pass_nueva)
        if ok:
            fila = self.servicio_usuario.encontrar_usuario_por_email(self.usuario_actual.email)
            if fila:
                id_usuario, nombre, email_usuario, hash_pass, rol = fila
                self.usuario_actual = Usuario(id_usuario, nombre, email_usuario, rol, hash_pass)
                self.password_hash = hash_pass
            else:
                self.password_hash = encriptar_contrasena(pass_nueva)
            return True
        return False

    def cambiar_nombre(self, nombre_nuevo):
        if not self.usuario_actual:
            return False
        ok = self.autenticacion.cambiar_nombre(self.usuario_actual.id_usuario, nombre_nuevo)
        if ok:
            fila = self.servicio_usuario.encontrar_usuario_por_email(self.usuario_actual.email)
            if fila:
                id_usuario, nombre, email_usuario, hash_pass, rol = fila
                self.usuario_actual = Usuario(id_usuario, nombre, email_usuario, rol, hash_pass)
            return True
        return False

