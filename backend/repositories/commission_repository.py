from typing import List, Optional, Tuple
import datetime
from database.conexion import ConexionBaseDatos


class CommissionRepository:
    def insert(self, user_id: int, descripcion: str) -> bool:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        fecha_actual = datetime.date.today()
        consulta = (
            "INSERT INTO comisiones (id_usuario, descripcion, estado, fecha) VALUES (%s, %s, 'Pendiente', %s)"
        )
        ok = conexion_db.ejecutar_consulta(consulta, (user_id, descripcion, fecha_actual))
        conexion_db.desconectar()
        return bool(ok)

    def list_by_user_id(self, user_id: int) -> List[Tuple]:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return []
        consulta = (
            "SELECT c.id_comision, u.nombre, c.fecha, c.estado, c.descripcion "
            "FROM comisiones c JOIN usuarios u ON c.id_usuario = u.id_usuario "
            "WHERE c.id_usuario = %s ORDER BY c.fecha DESC"
        )
        resultado = conexion_db.ejecutar_consulta(consulta, (user_id,))
        conexion_db.desconectar()
        return resultado or []

    def list_all_with_user(self) -> List[Tuple]:
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

    def get_state_by_id(self, commission_id: int) -> Optional[str]:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return None
        consulta = "SELECT estado FROM comisiones WHERE id_comision = %s"
        resultado = conexion_db.ejecutar_consulta(consulta, (commission_id,))
        conexion_db.desconectar()
        if resultado:
            return str(resultado[0][0])
        return None

    def mark_dispatched(self, commission_id: int) -> bool:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "UPDATE comisiones SET estado = 'Despachado' WHERE id_comision = %s"
        ok = conexion_db.ejecutar_consulta(consulta, (commission_id,))
        conexion_db.desconectar()
        return bool(ok)

    def has_commissions_for_user(self, user_id: int) -> bool:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "SELECT 1 FROM comisiones WHERE id_usuario = %s LIMIT 1"
        resultado = conexion_db.ejecutar_consulta(consulta, (user_id,))
        conexion_db.desconectar()
        return bool(resultado)
