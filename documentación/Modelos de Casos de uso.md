# Modelos de Casos de Uso (Logisticom)

## Alcance y Contexto
- **Sistema:** Gestión de comisiones con administración de usuarios y roles.  
- **Objetivo:** Registrar y administrar comisiones; gestionar usuarios y permisos.  

## Actores
- **Usuario:** Persona autenticada con rol usuario.  
- **Admin:** Persona autenticada con rol admin con privilegios administrativos.  

## Reglas de Negocio (RB)
- **RB1:** Autenticación por email y contraseña hasheada (SHA-256).  
- **RB2:** Autorización por rol (admin/usuario) para operaciones administrativas.  
- **RB3:** Ciclo de vida de comisión: Pendiente → Despachado.  
- **RB4:** Fecha de comisión registrada automáticamente en la creación.  
- **RB5:** Integridad lógica: evitar operaciones que dejen el sistema en estado inconsistente.  
- **RB6:** Política de contraseñas (mínimo de longitud y combinación alfanumérica).  

## Diagrama General de Casos de Uso
**Actores y Casos de Uso:**
- **Usuario:** Iniciar sesión, Cambiar nombre, Cambiar contraseña, Ingresar comisión, Ver mis comisiones  
- **Admin:** Registrar usuario, Ver todos los usuarios, Cambiar rol de usuario, Eliminar usuario, Ver todas las comisiones, Despachar comisión  

**Relaciones:**
- Usuario → Iniciar sesión, Cambiar nombre, Cambiar contraseña, Ingresar comisión, Ver mis comisiones  
- Admin → Registrar usuario, Ver todos los usuarios, Cambiar rol de usuario, Eliminar usuario, Ver todas las comisiones, Despachar comisión  

## Matriz de Trazabilidad (UC → Módulo/Implementación)

| UC     | Caso de Uso               | Módulo   | Puntos clave de implementación |
|--------|---------------------------|----------|--------------------------------|
| UC-L1  | Iniciar sesión            | Login    | Login.inicio_de_sesion         |
| UC-U5  | Cambiar nombre            | Login    | Login.cambiar_nombre           |
| UC-U6  | Cambiar contraseña        | Login    | Login.cambiar_pass             |
| UC-C1  | Ingresar comisión         | Comision | Comision.ingresar_comision     |
| UC-C2  | Ver mis comisiones        | Comision | Comision.listar_comisiones_usuario |
| UC-C3  | Ver todas las comisiones  | Comision | Comision.listar_comisiones_todos |
| UC-C4  | Despachar comisión        | Comision | Comision.despachar_comision   |
| UC-U1  | Registrar usuario         | Usuario  | Usuario.registrar_usuario      |
| UC-U2  | Ver todos los usuarios    | Usuario  | Usuario.listar_todos           |
| UC-U3  | Cambiar rol de usuario    | Usuario  | Usuario.cambiar_rol            |
| UC-U4  | Eliminar usuario          | Usuario  | Usuario.eliminar_usuario       |

---

# Casos de Uso por Módulo

## Módulo Login

![Caso de uso - Login](Caso%20de%20uso%20-%20Login.png "Diagrama de casos de uso del módulo Login")

### UC-L1: Iniciar sesión
- **Actor:** Usuario  
- **Propósito:** Acceder al sistema con credenciales válidas.  
- **Precondiciones:** Usuario registrado; contraseña hasheada almacenada (RB1).  
- **Disparador:** Usuario ingresa email y contraseña.  
- **Flujo principal:**  
  1. El usuario ingresa email y contraseña.  
  2. El sistema busca usuario por email.  
  3. El sistema hashea la contraseña ingresada y compara.  
  4. Si coincide, inicia sesión y carga usuario actual.  
- **Flujos alternos/Excepciones:**  
  - Hash no coincide → “Credenciales incorrectas”.  
- **Postcondiciones:**  
  - Éxito: Sesión iniciada; usuario actual en memoria.  
  - Garantía mínima: No se exponen contraseñas en claro.  
- **Reglas:** RB1, RB2  

### UC-U5: Cambiar nombre
- **Actor:** Usuario  
- **Propósito:** Actualizar su nombre.  
- **Precondiciones:** Usuario autenticado.  
- **Flujo principal:**  
  1. Ingresa nombre nuevo.  
  2. El sistema actualiza el nombre.  
- **Excepciones:** Error de persistencia.  
- **Postcondiciones:** Nombre actualizado.  

### UC-U6: Cambiar contraseña
- **Actor:** Usuario  
- **Propósito:** Actualizar su contraseña.  
- **Precondiciones:** Usuario autenticado; contraseña actual válida; nueva cumple política (RB6).  
- **Flujo principal:**  
  1. Ingresa contraseña actual, nueva y confirmación.  
  2. El sistema valida la actual (comparando hash).  
  3. Valida política; hashea nueva.  
  4. Actualiza contraseña.  
- **Excepciones:**  
  - Contraseña actual incorrecta → Mensaje y reintento.  
  - Nueva no válida → Mensaje y reintento.  
  - Error de persistencia.  
- **Postcondiciones:** Contraseña actualizada y hasheada.  
- **Reglas:** RB1, RB6  

---

## Módulo Usuario

![Caso de uso - Usuario](Caso%20de%20uso%20-%20Usuario.png "Diagrama de casos de uso del módulo Usuario")

### UC-U1: Registrar usuario
- **Actor:** Admin  
- **Propósito:** Crear un nuevo usuario con rol.  
- **Precondiciones:** Admin autenticado (RB2); email no registrado; rol válido.  
- **Flujo principal:**  
  1. Admin ingresa nombre, email, rol y contraseña inicial.  
  2. El sistema valida unicidad del email.  
  3. Resuelve id_rol por nombre.  
  4. Hashea la contraseña.  
  5. Inserta el usuario.  
- **Excepciones:**  
  - Email duplicado → Abortar con mensaje.  
  - Rol inválido → Abortar con mensaje.  
  - Error de persistencia.  
- **Postcondiciones:** Usuario persistido con rol asignado.  
- **Reglas:** RB1, RB2  

### UC-U2: Ver todos los usuarios
- **Actor:** Admin  
- **Propósito:** Listar usuarios con su rol.  
- **Precondiciones:** Admin autenticado (RB2).  
- **Flujo principal:**  
  1. Ejecuta consulta con JOIN usuarios ↔ roles.  
  2. Muestra id, nombre, email y rol.  
- **Excepciones:**  
  - Sin registros → “No hay usuarios”.  
  - Error de persistencia.  
- **Postcondiciones:** Lista visible en consola.  

### UC-U3: Cambiar rol de usuario
- **Actor:** Admin  
- **Propósito:** Actualizar el rol de un usuario.  
- **Precondiciones:** Admin autenticado; usuario existe; rol nuevo válido.  
- **Flujo principal:**  
  1. Selecciona usuario y rol nuevo.  
  2. El sistema resuelve id_rol y actualiza.  
- **Excepciones:** Usuario no encontrado; rol inválido; error de persistencia.  
- **Postcondiciones:** Rol actualizado.  
- **Reglas:** RB2  

### UC-U4: Eliminar usuario
- **Actor:** Admin  
- **Propósito:** Borrar un usuario.  
- **Precondiciones:** Admin autenticado; usuario existe.  
- **Flujo principal:**  
  1. Solicita confirmación.  
  2. Si confirma, elimina registro.  
- **Excepciones:**  
  - Cancelación.  
  - Usuario no encontrado; restricciones lógicas (RB5); error de persistencia.  
- **Postcondiciones:** Usuario eliminado.  
- **Reglas:** RB2, RB5  

---

## Módulo Comisión

![Caso de uso - Comisión](Caso%20de%20uso%20-%20Comisión.png "Diagrama de casos de uso del módulo Comisión")

### UC-C1: Ingresar comisión
- **Actor:** Usuario  
- **Propósito:** Registrar una nueva comisión en estado Pendiente.  
- **Precondiciones:** Usuario autenticado.  
- **Flujo principal:**  
  1. Ingresa descripción.  
  2. El sistema inserta con fecha actual (RB4) y estado Pendiente (RB3).  
- **Excepciones:** Error de persistencia.  
- **Postcondiciones:** Comisión creada.  
- **Reglas:** RB3, RB4  

### UC-C2: Ver mis comisiones
- **Actor:** Usuario  
- **Propósito:** Listar comisiones propias.  
- **Precondiciones:** Usuario autenticado.  
- **Flujo principal:**  
  1. Consulta JOIN comisiones ↔ usuarios filtrada por id_usuario.  
  2. Muestra ID, usuario, fecha, estado, descripción.  
- **Excepciones:**  
  - Sin registros → Mensaje informativo.  
  - Error de persistencia.  
- **Postcondiciones:** Lista visible en consola.  
- **Reglas:** RB2, RB3  

### UC-C3: Ver todas las comisiones
- **Actor:** Admin  
- **Propósito:** Listar comisiones de todos los usuarios.  
- **Precondiciones:** Admin autenticado (RB2).  
- **Flujo principal:**  
  1. Consulta JOIN comisiones ↔ usuarios.  
  2. Muestra ID, usuario, fecha, estado, descripción.  
- **Excepciones:**  
  - Sin registros → Mensaje informativo.  
  - Error de persistencia.  
- **Postcondiciones:** Lista visible en consola.  
- **Reglas:** RB2, RB3  

### UC-C4: Despachar comisión
- **Actor:** Admin  
- **Propósito:** Cambiar el estado a Despachado.  
- **Precondiciones:** Admin autenticado; comisión existe; estado actual ≠ Despachado.  
- **Flujo principal:**  
  1. Ingresa ID de comisión.  
  2. Verifica existencia y estado.  
  3. Actualiza estado a Despachado.  
- **Excepciones:**  
  - No encontrada → Mensaje “Comisión no encontrada”.  
  - Ya despachada → Mensaje y abortar.  
  - Error de persistencia.  
- **Postcondiciones:** Comisión en estado Despachado.  
- **Reglas:** RB3  

---

## Requisitos No Funcionales (NFR)
- **Seguridad:** Hash de contraseñas (RB1); no exponer credenciales ni datos sensibles.  
- **Usabilidad:** Flujos por consola con mensajes claros y validaciones básicas.  
- **Confiabilidad:** Manejo de errores y mensajes de excepción coherentes.  
- **Mantenibilidad:** Separación en módulos Login, Usuario, Comisión.  
