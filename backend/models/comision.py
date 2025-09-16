import datetime
from models.usuario import Usuario
from database.conexion import ConexionBaseDatos

class Comision:
    def ingresar_comision(id_usuario, descripcion):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        
        fecha_actual = datetime.date.today()
        
        consulta = "INSERT INTO comisiones (id_usuario, descripcion, estado, fecha) VALUES (%s, %s, 'Pendiente', %s)"
        
        if conexion_db.ejecutar_consulta(consulta, (id_usuario, descripcion, fecha_actual)):
            conexion_db.desconectar()
            return True
        else:
            conexion_db.desconectar()
            return False

    def listar_comisiones_usuario(id_usuario):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return []
        
        consulta = "SELECT c.id_comision, u.nombre, c.fecha, c.estado, c.descripcion FROM comisiones c JOIN usuarios u ON c.id_usuario = u.id_usuario WHERE c.id_usuario = %s ORDER BY c.fecha DESC"
        resultado = conexion_db.ejecutar_consulta(consulta, (id_usuario,))
        conexion_db.desconectar()
        
        return resultado

    def listar_comisiones_todos():
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return []
        
        consulta = "SELECT c.id_comision, u.nombre, c.fecha, c.estado, c.descripcion FROM comisiones c JOIN usuarios u ON c.id_usuario = u.id_usuario ORDER BY c.fecha DESC"
        resultado = conexion_db.ejecutar_consulta(consulta)
        conexion_db.desconectar()
        
        return resultado

    def despachar_comision(id_comision, id_usuario=None):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        
        if id_usuario:
            consulta = "SELECT estado FROM comisiones WHERE id_comision = %s AND id_usuario = %s"
            parametros = (id_comision, id_usuario)
        else:
            consulta = "SELECT estado FROM comisiones WHERE id_comision = %s"
            parametros = (id_comision,)
        
        resultado = conexion_db.ejecutar_consulta(consulta, parametros)
        
        if not resultado:
            print("Comisión no encontrada.")
            conexion_db.desconectar()
            return False
        
        estado_actual = resultado[0][0]
        if estado_actual == 'Despachado':
            print("Comisión ya despachada.")
            conexion_db.desconectar()
            return False
        
        consulta_actualizar = "UPDATE comisiones SET estado = 'Despachado' WHERE id_comision = %s"
        
        if conexion_db.ejecutar_consulta(consulta_actualizar, (id_comision,)):
            conexion_db.desconectar()
            return True
        else:
            conexion_db.desconectar()
            return False

