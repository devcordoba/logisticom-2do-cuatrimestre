# Diseño y Documentación de la Base de Datos

## Entidades Principales

- **Usuario**: representa a los individuos que interactúan con el sistema.
- **Rol**: determina los permisos y el nivel de acceso del usuario.
- **Comision**: solicitud generada por un usuario.

## Atributos de Cada Entidad

### *Usuarios*

- `id_usuario`: Identificador único (INT, AUTO_INCREMENT, PK).
- `nombre`: Nombre completo del usuario (VARCHAR(100), NOT NULL).
- `email`: Dirección de correo (VARCHAR(100), NOT NULL).
- `contrasena`: Hash de la contraseña SHA-256 (VARCHAR(64), NOT NULL).
- `id_rol`: Referencia al rol asignado (INT, FK, NOT NULL).

### *Roles*

- `id_rol`: Clave primaria (INT, AUTO_INCREMENT, PK).
- `nombre`: Nombre del rol (VARCHAR(50), NOT NULL).

### *Comisiones*

- `id_comision`: Identificador de la comisión (INT, AUTO_INCREMENT, PK).
- `id_usuario`: Usuario que realiza la comisión (INT, FK, NOT NULL).
- `fecha`: Fecha de creación (DATE, DEFAULT CURRENT_DATE).
- `estado`: Estado actual (VARCHAR(20), DEFAULT 'Pendiente').
- `descripcion`: Detalles de la comisión (VARCHAR(500)).

## Relaciones Entre Entidades

- **Usuario ↔ Rol**  
  Relación de **uno a muchos**.  
  Cada *Rol* puede estar asociado a varios *Usuarios*, pero cada *Usuario* tiene asignado solo un *Rol*.  
  _(Representación: `Usuarios }o--|| Roles`)_

- **Usuario ↔ Comisión**  
  Relación de **uno a muchos**.  
  Un *Usuario* puede registrar múltiples *Comisiones*, pero cada *Comisión* pertenece a un único *Usuario*.  
  _(Representación: `Usuarios ||--o{ Comisiones`)_

## Normalización

El modelo fue normalizado hasta **Tercera Forma Normal (3FN)** para evitar redundancias y dependencias innecesarias:

- Todos los atributos son atómicos (1FN).
- Se eliminaron dependencias parciales (2FN).
- Se eliminaron dependencias transitivas, separando responsabilidades conceptuales en distintas tablas (3FN).

## Modelo Relacional

```mermaid
erDiagram
    ROLES {
        int id_rol PK "AUTO_INCREMENT"
        varchar nombre "NOT NULL"
    }

    USUARIOS {
        int id_usuario PK "AUTO_INCREMENT"
        varchar nombre "NOT NULL"
        varchar email "NOT NULL"
        varchar contrasena "NOT NULL, SHA-256"
        int id_rol FK "NOT NULL"
    }

    COMISIONES {
        int id_comision PK "AUTO_INCREMENT"
        int id_usuario FK "NOT NULL"
        date fecha "DEFAULT CURRENT_DATE"
        varchar estado "DEFAULT 'Pendiente'"
        varchar descripcion "TEXT"
    }

    %% Relaciones
    ROLES ||--o{ USUARIOS : "asigna"
    USUARIOS ||--o{ COMISIONES : "crea"
```

## Diagrama de Clases

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
        +ejecutar_consulta(query, params) result
    }

    class Usuario {
        -id_usuario: int
        -nombre: str
        -email: str
        -rol: str
        -pass: str
        +registrar_usuario(nombre, email, rol, pass) bool
        +listar_todos() list
        +obtener_por_email(email) Usuario
        +obtener_por_id(id_usuario) Usuario
        +cambiar_rol(id_usuario, rol_nuevo) bool
        +eliminar_usuario(id_usuario) bool
    }

    class Login {
        -usuario_actual: Usuario
        -password_hash: str
        +inicio_de_sesion(email, password) bool
        +cambiar_pass(pass_actual, pass_nueva) bool
        +cambiar_nombre(nombre_nuevo) bool
    }

    class Comision {
        +ingresar_comision(id_usuario, descripcion) bool
        +listar_comisiones_usuario(id_usuario) list
        +listar_comisiones_todos() list
        +despachar_comision(id_comision, id_usuario) bool
    }

    class Menu {
        -login: Login
        +cambiar_rol_usuario() void
        +eliminar_usuario() void
        +registrar_usuario_admin() void
        +ver_menu() void
    }

    class Utils {
        +validar_contrasena(password) bool
        +encriptar_contrasena(passwd) str
    }

    %% Relaciones
    Usuario --> ConexionBaseDatos : usa
    Login --> Usuario : contiene
    Login --> ConexionBaseDatos : usa
    Comision --> ConexionBaseDatos : usa
    Menu --> Usuario : usa
    Menu --> Login : contiene
    Menu --> Comision : usa
    Menu --> Utils : usa
    Usuario --> Utils : usa
    Login --> Utils : usa
```

## Consideraciones de Diseño

- **Base de datos**: `logisticom_db` - nombre específico del proyecto
- **Roles en tabla separada**: mejora la escalabilidad y evita errores de tipeo o inconsistencias.
- **Contraseñas hasheadas**: se aplica SHA-256 antes del almacenamiento.

## Features

1. **Autenticación**: Los usuarios se autentican con email y contraseña encriptada.
2. **Autorización**: Los roles determinan qué operaciones puede realizar cada usuario.
3. **Auditoría**: Todas las comisiones registran fecha de creación automáticamente.
4. **Estados**: Las comisiones tienen un ciclo de vida (Pendiente → Despachado).
5. **Integridad**: Se mantiene consistencia de datos a nivel de aplicación.

## Datos de Prueba

```sql
-- Roles iniciales
INSERT INTO roles (nombre) VALUES ('admin'), ('usuario');

-- Usuarios de prueba
INSERT INTO usuarios (nombre, email, contrasena, id_rol) 
VALUES 
  ('Admin', 'admin@abc.com', SHA2('admin123', 256), 1),
  ('Juan', 'juan@abc.com', SHA2('user123', 256), 2);
```

## Estructura de Archivos

- `proyecto_base_de_datos.sql`: Script de creación de la base de datos
- `CRUD.sql`: Ejemplos de operaciones CRUD
- `diagrams/diagrama-entidad-relacion.md`: Diagrama E-R en Mermaid
- `diagrams/diagrama-clases.md`: Diagrama de clases en Mermaid
