from models.usuario import Usuario
from database.conexion import ConexionBaseDatos
from utils.utils import encriptar_contrasena

class Login:
    def __init__(self):
        self.usuario_actual = None
        self.password_hash = None

    def inicio_de_sesion(self, email, password):
        usuario = Usuario.obtener_por_email(email)
        if usuario:
            password_enc = encriptar_contrasena(password)
            if password_enc == usuario.password:
                self.usuario_actual = usuario
                self.password_hash = password_enc
                return True
        return False

    def cambiar_pass(self, pass_actual, pass_nueva):
        if encriptar_contrasena(pass_actual) == self.password_hash:
            pass_nueva_encriptada = encriptar_contrasena(pass_nueva)
            
            conexion_db = ConexionBaseDatos()
            if not conexion_db.conectar():
                return False
            
            consulta = "UPDATE usuarios SET contrasena = %s WHERE id_usuario = %s"
            if conexion_db.ejecutar_consulta(consulta, (pass_nueva_encriptada, self.usuario_actual.id_usuario)):
                self.usuario_actual.password = pass_nueva_encriptada
                self.password_hash = pass_nueva_encriptada
                conexion_db.desconectar()
                return True
            else:
                conexion_db.desconectar()
                return False
        else:
            return False

    def cambiar_nombre(self, nombre_nuevo):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        
        consulta = "UPDATE usuarios SET nombre = %s WHERE id_usuario = %s"
        if conexion_db.ejecutar_consulta(consulta, (nombre_nuevo, self.usuario_actual.id_usuario)):
            self.usuario_actual.nombre = nombre_nuevo
            conexion_db.desconectar()
            return True
        else:
            conexion_db.desconectar()
            return False

