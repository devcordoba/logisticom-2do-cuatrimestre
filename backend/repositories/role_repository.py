from typing import Optional
from database.conexion import ConexionBaseDatos


class RoleRepository:
    def get_id_by_name(self, role_name: str) -> Optional[int]:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return None
        consulta = "SELECT id_rol FROM roles WHERE nombre = %s"
        resultado = conexion_db.ejecutar_consulta(consulta, (role_name,))
        conexion_db.desconectar()
        if resultado:
            return int(resultado[0][0])
        return None

    def list_roles(self):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return []
        consulta = "SELECT id_rol, nombre FROM roles ORDER BY id_rol"
        resultado = conexion_db.ejecutar_consulta(consulta)
        conexion_db.desconectar()
        return resultado or []
