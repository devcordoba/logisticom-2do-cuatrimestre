from models.login import Login
from menu.menu import Menu
from models.comision import Comision
from models.usuario import Usuario
from utils.utils import validar_contrasena

def main():
    while True:
        login = Login()
        print("\n=== Sistema de gestion de comisiones ===")
        print("\n=== Iniciar sesion ===\n")
        email = input("Email: ")
        password = input("Contraseña: ")

        if login.inicio_de_sesion(email, password):
            menu = Menu(login)
            while True:
                menu.ver_menu()
                opcion = input("\nOpcion: ")
                
                if opcion == '0':
                    print("\nSaliendo del sistema...")
                    break
                elif opcion == '1':
                    descripcion = input("\nDescripcion de la comision: ")
                    if Comision.ingresar_comision(login.usuario_actual.id_usuario, descripcion):
                        print("\nComision ingresada.")
                    else:
                        print("Error.")
                elif opcion == '2':
                    comisiones = Comision.listar_comisiones_usuario(login.usuario_actual.id_usuario)
                    if comisiones:
                        print("\n=== Mis Comisiones ===")
                        for i, comision in enumerate(comisiones, start=1):
                            id_comision, nombre, fecha, estado, descripcion = comision
                            print(f"{i}. ID: {id_comision}, Usuario: {nombre}, Fecha: {fecha}, Estado: {estado}, Descripcion: {descripcion}")
                    else:
                        print("No tienes comisiones.")
                elif opcion == '3':
                    nombre_nuevo = input("\nNuevo nombre: ")
                    if login.cambiar_nombre(nombre_nuevo):
                        print("Nombre actualizado.")
                    else:
                        print("Error.")
                elif opcion == '4':
                    while True:
                        pass_actual = input("Pass actual: ")
                        pass_nueva = input("Nueva pass: ")
                        pass_confirmar = input("Confirmar pass: ")

                        if not validar_contrasena(pass_nueva):
                            print("La pass debe tener al menos 6 caracteres, incluir letras y numeros.")
                            continue
                        elif pass_nueva != pass_confirmar:
                            print("Las pass no coinciden.")
                            continue
                        else:
                            if login.cambiar_pass(pass_actual, pass_nueva):
                                print("Pass actualizada.")
                                break
                            else:
                                print("Error: pass actual incorrecta.")
                                continue
                elif opcion == '5':
                    if login.usuario_actual.rol == 'admin':
                        menu.registrar_usuario_admin()
                    else:
                        print("Opcion no valida.")
                elif opcion == '6':
                    if login.usuario_actual.rol == 'admin':
                        todas_comisiones = Comision.listar_comisiones_todos()
                        if todas_comisiones:
                            print("\n=== Todas las Comisiones ===")
                            for i, comision in enumerate(todas_comisiones):
                                id_comision, nombre, fecha, estado, descripcion = comision
                                print(f"\n{i+1}. ID: {id_comision}, Usuario: {nombre}, Fecha: {fecha}, Estado: {estado}, Descripcion: {descripcion}")
                        else:
                            print("No hay comisiones.")
                    else:
                        print("Opcion no valida.")
                elif opcion == '7':
                    if login.usuario_actual.rol == 'admin':
                        try:
                            id_comision_despachar = int(input("\nID de la comision a despachar: "))
                            if Comision.despachar_comision(id_comision_despachar):
                                print("\nDespachado correctamente.")
                            else:
                                print("Error.")
                        except:
                            print("ID invalido.")
                    else:
                        print("Opcion no valida.")
                elif opcion == '8':
                    if login.usuario_actual.rol == 'admin':
                        usuarios = Usuario.listar_todos()
                        if usuarios:
                            print("\n=== Lista de usuarios ===")
                            for i, usuario in enumerate(usuarios, start=1):
                                id_usuario, nombre, email, rol = usuario
                                print(f"{i}. ID: {id_usuario}, Nombre: {nombre}, Email: {email}, Rol: {rol}")
                        else:
                            print("No hay usuarios.")
                    else:
                        print("Opcion no valida.")
                elif opcion == '9':
                    if login.usuario_actual.rol == 'admin':
                        menu.cambiar_rol_usuario()
                    else:
                        print("Opcion no valida.")
                elif opcion == '10':
                    if login.usuario_actual.rol == 'admin':
                        menu.eliminar_usuario()
                    else:
                        print("Opcion no valida.")
                else:
                    print("Opcion no valida.")
        else:
            print("Credenciales incorrectas. Intente de nuevo.")

if __name__ == "__main__":
    main()