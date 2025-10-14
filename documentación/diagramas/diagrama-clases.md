# Diagrama de Clases - Logisticom (Sistema de Comisiones)

```mermaid
classDiagram
    class ConexionBaseDatos {
        -connection: mysql.connector
        -host: str
        -database: str
        -user: str
        -password: str
        +conectar() bool
        +desconectar() void
        +ejecutar_consulta(query, parametros) result
    }

    class Usuario {
        -id_usuario: int
        -nombre: str
        -email: str
        -rol: str
        -password: str
    }

    class Login {
        -usuario_actual: Usuario
        -password_hash: str
        +inicio_de_sesion(email, password) bool
        +cambiar_pass(pass_actual, pass_nueva) bool
        +cambiar_nombre(nombre_nuevo) bool
    }

    class Menu {
        -login: Login
        +cambiar_rol_usuario() void
        +eliminar_usuario() void
        +registrar_usuario_admin() void
        +ver_menu() void
    }

    class ServicioAutenticacion {
        +iniciar_sesion(email, password) Usuario
        +cambiar_contrasena(id_usuario, pass_actual, pass_nueva) bool
        +cambiar_nombre(id_usuario, nombre_nuevo) bool
    }

    class ServicioUsuario {
        +registrar_usuario(nombre, email, rol, password) bool
        +listar_todos() list
        +cambiar_rol(id_usuario, rol_nuevo) bool
        +eliminar_usuario(id_usuario) bool
    }

    class ServicioComision {
        +crear_comision(id_usuario, descripcion) bool
        +listar_comisiones_usuario(id_usuario) list
        +listar_todas() list
        +despachar_comision(id_comision) bool
    }

    class RepositorioUsuario {
        +obtener_por_email(email) tuple
        +obtener_por_id(id_usuario) tuple
        +listar_todos_con_roles() list
        +insertar_usuario(nombre, email, hash, id_rol) bool
        +actualizar_rol(id_usuario, id_rol) bool
        +actualizar_nombre(id_usuario, nombre) bool
        +actualizar_contrasena(id_usuario, hash) bool
        +eliminar_usuario(id_usuario) bool
    }

    class RepositorioRol {
        +obtener_id_por_nombre(rol) int
        +listar_roles() list
    }

    class RepositorioComision {
        +insertar(id_usuario, descripcion) bool
        +listar_por_id_usuario(id_usuario) list
        +listar_todas_con_usuario() list
        +obtener_estado_por_id(id_comision) str
        +marcar_despachado(id_comision) bool
    }

    class Utils {
        +validar_contrasena(password) bool
        +encriptar_contrasena(passwd) str
    }

    %% Relaciones (capa a capa)
    Menu --> Login : contiene
    Menu --> ServicioUsuario : usa
    Menu --> ServicioComision : usa
    Login --> ServicioAutenticacion : usa

    ServicioAutenticacion --> RepositorioUsuario : usa
    ServicioUsuario --> RepositorioUsuario : usa
    ServicioUsuario --> RepositorioRol : usa
    ServicioUsuario --> RepositorioComision : valida/elimina
    ServicioComision --> RepositorioComision : usa

    RepositorioUsuario --> ConexionBaseDatos : usa
    RepositorioRol --> ConexionBaseDatos : usa
    RepositorioComision --> ConexionBaseDatos : usa

    ServicioAutenticacion --> Utils : usa
    ServicioUsuario --> Utils : usa
```
