from database.conexion import ConexionBaseDatos
from utils.utils import encriptar_contrasena

class Usuario:
    def __init__(self, id_usuario, nombre, email, rol, pass_hash=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.rol = rol
        self.password = pass_hash

    def registrar_usuario(nombre, email, rol, password):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        
        consulta = "SELECT id_usuario FROM usuarios WHERE email = %s"
        resultado = conexion_db.ejecutar_consulta(consulta, (email,))
        
        if resultado:
            print("El email ya está registrado.")
            conexion_db.desconectar()
            return False
        
        consulta_rol = "SELECT id_rol FROM roles WHERE nombre = %s"
        resultado_rol = conexion_db.ejecutar_consulta(consulta_rol, (rol,))
        
        if not resultado_rol:
            print("Rol no válido.")
            conexion_db.desconectar()
            return False
        
        id_rol = resultado_rol[0][0]
        
        pass_encriptada = encriptar_contrasena(password)
        
        consulta_insertar = "INSERT INTO usuarios (nombre, email, contrasena, id_rol) VALUES (%s, %s, %s, %s)"
        
        if conexion_db.ejecutar_consulta(consulta_insertar, (nombre, email, pass_encriptada, id_rol)):
            conexion_db.desconectar()
            return True
        else:
            conexion_db.desconectar()
            return False

    def listar_todos():
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return []
        
        consulta = "SELECT u.id_usuario, u.nombre, u.email, r.nombre as rol FROM usuarios u JOIN roles r ON u.id_rol = r.id_rol ORDER BY u.id_usuario"
        resultado = conexion_db.ejecutar_consulta(consulta)
        conexion_db.desconectar()
        
        return resultado

    def obtener_por_email(email):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return None
        
        consulta = """
        SELECT u.id_usuario, u.nombre, u.email, u.contrasena, r.nombre as rol
        FROM usuarios u
        JOIN roles r ON u.id_rol = r.id_rol
        WHERE u.email = %s
        """
        resultado = conexion_db.ejecutar_consulta(consulta, (email,))
        conexion_db.desconectar()

        if resultado:
            id_usuario, nombre, email_usuario, password, rol = resultado[0]
            return Usuario(id_usuario, nombre, email_usuario, rol, password)

        return None

    def obtener_por_id(id_usuario):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return None
        
        consulta = """
        SELECT u.id_usuario, u.nombre, u.email, u.contrasena, r.nombre as rol
        FROM usuarios u
        JOIN roles r ON u.id_rol = r.id_rol
        WHERE u.id_usuario = %s
        """
        resultado = conexion_db.ejecutar_consulta(consulta, (id_usuario,))
        conexion_db.desconectar()

        if resultado:
            id_usuario_obj, nombre, email_usuario, password, rol = resultado[0]
            return Usuario(id_usuario_obj, nombre, email_usuario, rol, password)

        return None


    def cambiar_rol(id_usuario, rol_nuevo):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        
        consulta_rol = "SELECT id_rol FROM roles WHERE nombre = %s"
        resultado_rol = conexion_db.ejecutar_consulta(consulta_rol, (rol_nuevo,))
        
        if not resultado_rol:
            print("Rol no válido.")
            conexion_db.desconectar()
            return False
        
        id_rol = resultado_rol[0][0]
        
        consulta_actualizar = "UPDATE usuarios SET id_rol = %s WHERE id_usuario = %s"
        
        if conexion_db.ejecutar_consulta(consulta_actualizar, (id_rol, id_usuario)):
            conexion_db.desconectar()
            return True
        else:
            conexion_db.desconectar()
            return False

    def eliminar_usuario(id_usuario):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        
        consulta = "DELETE FROM usuarios WHERE id_usuario = %s"
        
        if conexion_db.ejecutar_consulta(consulta, (id_usuario,)):
            conexion_db.desconectar()
            return True
        else:
            conexion_db.desconectar()
            return False