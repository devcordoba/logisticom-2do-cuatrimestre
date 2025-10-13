from typing import List, Optional, Tuple
from database.conexion import ConexionBaseDatos


class UserRepository:
    def get_by_email(self, email: str) -> Optional[Tuple]:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return None
        consulta = (
            "SELECT u.id_usuario, u.nombre, u.email, u.contrasena, r.nombre as rol "
            "FROM usuarios u JOIN roles r ON u.id_rol = r.id_rol WHERE u.email = %s"
        )
        resultado = conexion_db.ejecutar_consulta(consulta, (email,))
        conexion_db.desconectar()
        return resultado[0] if resultado else None

    def get_by_id(self, user_id: int) -> Optional[Tuple]:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return None
        consulta = (
            "SELECT u.id_usuario, u.nombre, u.email, u.contrasena, r.nombre as rol "
            "FROM usuarios u JOIN roles r ON u.id_rol = r.id_rol WHERE u.id_usuario = %s"
        )
        resultado = conexion_db.ejecutar_consulta(consulta, (user_id,))
        conexion_db.desconectar()
        return resultado[0] if resultado else None

    def list_all_with_roles(self) -> List[Tuple]:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return []
        consulta = (
            "SELECT u.id_usuario, u.nombre, u.email, r.nombre as rol "
            "FROM usuarios u JOIN roles r ON u.id_rol = r.id_rol ORDER BY u.id_usuario"
        )
        resultado = conexion_db.ejecutar_consulta(consulta)
        conexion_db.desconectar()
        return resultado or []

    def email_exists(self, email: str) -> bool:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "SELECT 1 FROM usuarios WHERE email = %s"
        resultado = conexion_db.ejecutar_consulta(consulta, (email,))
        conexion_db.desconectar()
        return bool(resultado)

    def insert_user(self, nombre: str, email: str, pass_hash: str, id_rol: int) -> bool:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = (
            "INSERT INTO usuarios (nombre, email, contrasena, id_rol) VALUES (%s, %s, %s, %s)"
        )
        ok = conexion_db.ejecutar_consulta(consulta, (nombre, email, pass_hash, id_rol))
        conexion_db.desconectar()
        return bool(ok)

    def update_role(self, user_id: int, id_rol: int) -> bool:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "UPDATE usuarios SET id_rol = %s WHERE id_usuario = %s"
        ok = conexion_db.ejecutar_consulta(consulta, (id_rol, user_id))
        conexion_db.desconectar()
        return bool(ok)

    def update_name(self, user_id: int, nombre_nuevo: str) -> bool:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "UPDATE usuarios SET nombre = %s WHERE id_usuario = %s"
        ok = conexion_db.ejecutar_consulta(consulta, (nombre_nuevo, user_id))
        conexion_db.desconectar()
        return bool(ok)

    def update_password(self, user_id: int, pass_hash: str) -> bool:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "UPDATE usuarios SET contrasena = %s WHERE id_usuario = %s"
        ok = conexion_db.ejecutar_consulta(consulta, (pass_hash, user_id))
        conexion_db.desconectar()
        return bool(ok)

    def delete_user(self, user_id: int) -> bool:
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "DELETE FROM usuarios WHERE id_usuario = %s"
        ok = conexion_db.ejecutar_consulta(consulta, (user_id,))
        conexion_db.desconectar()
        return bool(ok)
