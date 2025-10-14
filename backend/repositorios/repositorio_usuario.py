from database.conexion import ConexionBaseDatos


class RepositorioUsuario:
    def obtener_por_email(self, email):
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

    def obtener_por_id(self, id_usuario):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return None
        consulta = (
            "SELECT u.id_usuario, u.nombre, u.email, u.contrasena, r.nombre as rol "
            "FROM usuarios u JOIN roles r ON u.id_rol = r.id_rol WHERE u.id_usuario = %s"
        )
        resultado = conexion_db.ejecutar_consulta(consulta, (id_usuario,))
        conexion_db.desconectar()
        return resultado[0] if resultado else None

    def listar_todos_con_roles(self):
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

    def existe_email(self, email):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "SELECT 1 FROM usuarios WHERE email = %s"
        resultado = conexion_db.ejecutar_consulta(consulta, (email,))
        conexion_db.desconectar()
        return bool(resultado)

    def insertar_usuario(self, nombre, email, hash_pass, id_rol):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = (
            "INSERT INTO usuarios (nombre, email, contrasena, id_rol) VALUES (%s, %s, %s, %s)"
        )
        ok = conexion_db.ejecutar_consulta(consulta, (nombre, email, hash_pass, id_rol))
        conexion_db.desconectar()
        return bool(ok)

    def actualizar_rol(self, id_usuario, id_rol):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "UPDATE usuarios SET id_rol = %s WHERE id_usuario = %s"
        ok = conexion_db.ejecutar_consulta(consulta, (id_rol, id_usuario))
        conexion_db.desconectar()
        return bool(ok)

    def actualizar_nombre(self, id_usuario, nombre_nuevo):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "UPDATE usuarios SET nombre = %s WHERE id_usuario = %s"
        ok = conexion_db.ejecutar_consulta(consulta, (nombre_nuevo, id_usuario))
        conexion_db.desconectar()
        return bool(ok)

    def actualizar_contrasena(self, id_usuario, hash_pass):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "UPDATE usuarios SET contrasena = %s WHERE id_usuario = %s"
        ok = conexion_db.ejecutar_consulta(consulta, (hash_pass, id_usuario))
        conexion_db.desconectar()
        return bool(ok)

    def eliminar_usuario(self, id_usuario):
        conexion_db = ConexionBaseDatos()
        if not conexion_db.conectar():
            return False
        consulta = "DELETE FROM usuarios WHERE id_usuario = %s"
        ok = conexion_db.ejecutar_consulta(consulta, (id_usuario,))
        conexion_db.desconectar()
        return bool(ok)
