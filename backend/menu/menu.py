from models.usuario import Usuario
from models.login import Login
from models.comision import Comision
from utils.utils import validar_contrasena

class Menu:
    def __init__(self, login):
        self.login = login

    def cambiar_rol_usuario(self):
        print("\nCambiar rol de usuario")
        email_usuario = input("Email del usuario a modificar: ")
        usuario_encontrado = Usuario.obtener_por_email(email_usuario)
        if not usuario_encontrado:
            print("Usuario no encontrado.")
            return

        while True:
            rol_nuevo = input("Nuevo rol (admin/usuario): ")
            if rol_nuevo in ('admin', 'usuario'):
                break
            print("Rol invalido. Intente de nuevo.")

        if Usuario.cambiar_rol(usuario_encontrado.id_usuario, rol_nuevo):
            print("Rol cambiado correctamente.")
        else:
            print("Error al cambiar rol.")

    def eliminar_usuario(self):
        print("\nEliminar usuario")
        email_usuario = input("Email del usuario a eliminar: ")
        usuario_encontrado = Usuario.obtener_por_email(email_usuario)
        if not usuario_encontrado:
            print("Usuario no encontrado.")
            return

        confirmacion = input(
            f"Seguro que desea eliminar al usuario {usuario_encontrado.nombre} "
            f"({usuario_encontrado.email})? (s/n): "
        )
        if confirmacion.lower() == 's':
            if Usuario.eliminar_usuario(usuario_encontrado.id_usuario):
                print("Usuario eliminado correctamente.")
            else:
                print("Error al eliminar usuario.")
        else:
            print("Eliminación cancelada.")

    def registrar_usuario_admin(self):
        print("\nRegistrar nuevo usuario")
        nombre_usuario = input("Nombre: ")
        email_usuario = input("Email: ")

        while True:
            rol_usuario = input("Rol (admin/usuario): ")
            if rol_usuario in ('admin', 'usuario'):
                break
            print("Rol invalido. Intente de nuevo.")

        while True:
            pass_inicial = input("Pass inicial: ")
            if not validar_contrasena(pass_inicial):
                print("La pass debe tener al menos 6 caracteres, incluir letras y numeros.")
                continue

            pass_confirmar = input("Confirmar pass: ")
            if pass_inicial != pass_confirmar:
                print("Las pass no coinciden. Intente de nuevo.")
                continue

            break

        if Usuario.registrar_usuario(nombre_usuario, email_usuario, rol_usuario, pass_inicial):
            print("Usuario registrado correctamente.")
        else:
            print("Error al registrar usuario.")

    def ver_menu(self):
        usuario = self.login.usuario_actual
        print(f"\nBienvenido/a, {usuario.nombre} ({usuario.rol})\n")
        print("1. Ingresar comisión")
        print("2. Ver mis comisiones")
        print("3. Cambiar nombre")
        print("4. Cambiar pass")

        if usuario.rol == 'admin':
            print("\n====== Menú administrativo ======\n")
            print("5. Registrar nuevo usuario")
            print("6. Ver todas las comisiones")
            print("7. Despachar comisión")
            print("8. Ver todos los usuarios")
            print("9. Cambiar rol de usuario")
            print("10. Eliminar usuario")
            print("\n=================================\n")

        print("0. Salir")