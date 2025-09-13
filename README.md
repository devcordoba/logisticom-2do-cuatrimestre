# LogistiCom

---

# LogistiCom - Sistema de Gestión de Comisiones

Sistema simple de gestion de comisiones hecho en Python con MySQL.

## Descripción

**LogistiCom** es un sistema de gestión orientado a empresas que trabajan exclusivamente con comisiones de paquetería.  
El objetivo principal del sistema es permitir la visualización clara y organizada de los datos relacionados a cada comisión, incluyendo:

- Fechas de inicio y entrega
- Cantidad de paquetes
- Montos asociados
- Direcciones de origen y destino
- Estado de la comisión (en curso, entregado, etc.)
- Vehículo utilizado

El sistema busca facilitar la administración diaria, la trazabilidad de envíos y el control financiero básico de la empresa.

## ✔️ Funcionalidades agregadas / ❌ Funcionalidades planeadas o que están en progreso

✔️​​ Registro y Login con autenticación de usuarios

✔️ Gestión de Usuarios

✔️ Gestión de Comisiones o pedidos

❌ Gestión de Viajes

❌ Dashboard con indicadores clave

❌ Gestión de Vehículos y Mantenimiento

❌ Visualización de Carteras (ingresos y egresos)

❌ Notificaciones internas

❌ Adaptado como Web App (uso optimizado desde dispositivos móviles)

## Usuarios

- **Administradores:** responsables de gestionar y supervisar las comisiones, viajes, y finanzas de la empresa.
- **Usuarios:** encargados de realizar las comisiones y consultar sus asignaciones desde el sistema.

---

## Como usar

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Crear la base de datos:
- Ejecutar el archivo proyecto_db.sql en MySQL

3. Ejecutar el programa:
```bash
python main.py
```

## Usuarios de prueba

- Admin: admin@abc.com / admin123
- Usuario: juan@abc.com / user123

---

## Funciones

### Usuario normal:
- Ver sus datos
- Cambiar nombre y contraseña
- Ingresar comisiones
- Ver sus comisiones

### Admin:
- Todo lo anterior
- Ver todos los usuarios
- Cambiar roles
- Eliminar usuarios
- Ver todas las comisiones
- Despachar comisiones

---

## Archivos

### Backend

- main.py - programa principal
- models/ - clases de usuario, login y comision
- database/ - conexion a MySQL
- menu/ - menus del sistema
- utils/ - validaciones
- proyecto_db.sql - script de base de datos

### Documentación

- Diagrama de clases
- Diagrama DER
- Documento IEEE 830

### Frontend

- css/ - directorio con estilos para HTML
- img/ - imagenes
- js/ - JavaScript
- *.html - archivos varios de paginas web de logisticom

---

## Equipo de desarrollo
| Nombre | Rol |
|--------|-----|
| Tomás Agustín Huespe | Developer |
| Ángel Nicolás Rivero | Developer |
| Verónica Analía Gagliardi | Developer |
| Tobias Molina | Developer |
| Gonzalo Nicolás Quiroga | Product Owner/Developer |
| Lanfranco Darel Caballero | Scrum Master/Developer |

---

## Tecnologías
- Lenguajes/herramientas: XAMPP, Docker, LAMP
- Base de datos: MySQL 
- Control de versiones: GitHub  

---

## Estado del Proyecto

🟡 El proyecto se encuentra en la etapa de desarrollo/sprint 1, véase la rama `develop` para ver los cambios 

## Materia

Este proyecto fue desarrollado como parte de la materia **Iniciación a la programación y base de datos** de la carrera **Tecnicatura Superior en Desarrollo Web y Aplicaciones Digitales**.
