import datetime
from database.conexion import ConexionBaseDatos


class RepositorioComision:
    def insertar(self, id_usuario, descripcion):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        fecha_actual = datetime.date.today()
        consulta = (
            "INSERT INTO comisiones (id_usuario, descripcion, estado, fecha) VALUES (%s, %s, 'Pendiente', %s)"
        )
        ok = conexion_db.ejecutar_consulta(consulta, (id_usuario, descripcion, fecha_actual))
        conexion_db.desconectar()
        return bool(ok)

    def listar_por_id_usuario(self, id_usuario):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return []
        consulta = (
            "SELECT c.id_comision, u.nombre, c.fecha, c.estado, c.descripcion "
            "FROM comisiones c JOIN usuarios u ON c.id_usuario = u.id_usuario "
            "WHERE c.id_usuario = %s ORDER BY c.fecha DESC"
        )
        resultado = conexion_db.ejecutar_consulta(consulta, (id_usuario,))
        conexion_db.desconectar()
        return resultado or []

    def listar_todas_con_usuario(self):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return []
        consulta = (
            "SELECT c.id_comision, u.nombre, c.fecha, c.estado, c.descripcion "
            "FROM comisiones c JOIN usuarios u ON c.id_usuario = u.id_usuario ORDER BY c.fecha DESC"
        )
        resultado = conexion_db.ejecutar_consulta(consulta)
        conexion_db.desconectar()
        return resultado or []

    def obtener_estado_por_id(self, id_comision):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return None
        consulta = "SELECT estado FROM comisiones WHERE id_comision = %s"
        resultado = conexion_db.ejecutar_consulta(consulta, (id_comision,))
        conexion_db.desconectar()
        if resultado:
            return str(resultado[0][0])
        return None

    def marcar_despachado(self, id_comision):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "UPDATE comisiones SET estado = 'Despachado' WHERE id_comision = %s"
        ok = conexion_db.ejecutar_consulta(consulta, (id_comision,))
        conexion_db.desconectar()
        return bool(ok)

    def tiene_comisiones_de_usuario(self, id_usuario):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "SELECT 1 FROM comisiones WHERE id_usuario = %s LIMIT 1"
        resultado = conexion_db.ejecutar_consulta(consulta, (id_usuario,))
        conexion_db.desconectar()
        return bool(resultado)
