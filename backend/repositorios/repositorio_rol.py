from typing import Optional
from database.conexion import ConexionBaseDatos


class RepositorioRol:
    def obtener_id_por_nombre(self, rol: str) -> Optional[int]:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return None
        consulta = "SELECT id_rol FROM roles WHERE nombre = %s"
        resultado = conexion_db.ejecutar_consulta(consulta, (rol,))
        conexion_db.desconectar()
        if resultado:
            return int(resultado[0][0])
        return None

    def listar_roles(self):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return []
        consulta = "SELECT id_rol, nombre FROM roles ORDER BY id_rol"
        resultado = conexion_db.ejecutar_consulta(consulta)
        conexion_db.desconectar()
        return resultado or []
