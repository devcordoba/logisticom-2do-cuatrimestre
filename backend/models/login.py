from models.usuario import Usuario
from utils.utils import encriptar_contrasena
from servicios.servicio_autenticacion import ServicioAutenticacion

class Login:
    def __init__(self):
        self.usuario_actual = None
        self.password_hash = None
        self.autenticacion = ServicioAutenticacion()

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
            pass_nueva_encriptada = encriptar_contrasena(pass_nueva)
            self.usuario_actual.password = pass_nueva_encriptada
            self.password_hash = pass_nueva_encriptada
            return True
        return False

    def cambiar_nombre(self, nombre_nuevo):
        if not self.usuario_actual:
            return False
        ok = self.autenticacion.cambiar_nombre(self.usuario_actual.id_usuario, nombre_nuevo)
        if ok:
            self.usuario_actual.nombre = nombre_nuevo
            return True
        return False

