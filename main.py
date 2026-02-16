"""
Proyecto ABP 4 - Gestión Inteligente de Clientes
[Autor]: Cristian Vargas
[Fecha]: 2026-02
"""
import os
from gestor.gestor_clientes import GestorClientes
from persist.persist import PersistJSON
from utils.logger import Logger
from utils.functions import menu, type_client
from utils.exceptions import EmailInvalidError, PhoneInvalidError
from models.cliente_regular import ClienteRegular
from models.cliente_premium import ClientePremium
from models.cliente_corporativo import ClienteCorporativo


def main():

    # Ruta que obtiene la carpeta donde esta el archivo
    BASE_DIR = os.path.dirname(__file__)

    log_path = os.path.join(BASE_DIR, "data", "logs.txt")
    json_path = os.path.join(BASE_DIR, "data", "clientes.json")

    logger = Logger(log_path)
    persist = PersistJSON(json_path)

    gestor = GestorClientes(persist,logger)
    gestor.load()

    # Con esto averigumos cual es el ultimo ID registrado en el JSON de clientes
    ultimo_id = max((cliente.id for cliente in gestor.clientes), default=0)

    while True:
        try:
            print("""
====================================
== GESTOR INTELIGENTE DE CLIENTES ==
====================================
""")
            menu()
            option = int(input("Ingrese una opción: "))

            if option == 1:
                
                id_cliente = ultimo_id + 1

                print("")
                print(f"Agregar cliente con ID: {id_cliente}")

                name = input("Ingrese nombre: ")
                email = input("Ingrese email: ")
                phone = input("Ingrese teléfono: (+56 9) ")

                while True:
                    try:
                        type_client()
                        option_type = int(input("Ingrese una opción: "))

                        if option_type == 1:
                            cliente = ClienteRegular(
                                id_cliente,
                                name,
                                email,
                                phone,
                                10.0
                            )
                            break
                        elif option_type == 2:
                            cliente = ClientePremium(
                                id_cliente,
                                name,
                                email,
                                phone,
                                0
                            )
                            break
                        elif option_type == 3:
                            opt = input("Nombre de empresa: ")
                            cliente = ClienteCorporativo(
                                id_cliente,
                                name,
                                email,
                                phone,
                                opt
                            )
                            break
                        else:
                            print("Opción invalida")
                            continue
                    except ValueError:
                        print("Ingresar opción valida")
                        continue
                try:
                    add_c = gestor.add_cliente(cliente)
                    if add_c:
                        gestor.save()

                        print("")
                        print("Cliente Ingresado con exito")
                        input("Presione una tecla para continuar...")

                except EmailInvalidError as e:
                    print(f"[ERROR] {e}")
                    print("== NO SE GUARDO EL CLIENTE ==")
                    input("Presione una tecla para continuar...")

                except PhoneInvalidError as e:
                    print(f"[ERROR] {e}")
                    print("== NO SE GUARDO EL CLIENTE ==")
                    input("Presione una tecla para continuar...")
                    
            elif option == 2:
                clientes = gestor.list_clientes()

                for cliente in clientes:
                    print(cliente)

                print("")
                input("Presione una tecla para continuar...")
            elif option == 3:
                index = int(input("Ingrese el ID del cliente a modificar: "))
                gestor.update_cliente(index)
            elif option == 4:
                index = int(input("Ingrese el ID del cliente a eliminar: "))
                gestor.del_cliente(index)
            elif option == 5:
                print(f"Hasta pronto")
                break
            else:
                print("Ingresar opción valida")
                continue

        except ValueError:
            print("Ingresar opción valida")
            continue

if __name__ == "__main__":
    main()