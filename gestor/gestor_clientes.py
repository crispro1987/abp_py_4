from models.cliente import Cliente
from utils.validate import Validate
from utils.exceptions import EmailInvalidError, PhoneInvalidError

from models.cliente_regular import ClienteRegular
from models.cliente_premium import ClientePremium
from models.cliente_corporativo import ClienteCorporativo

class GestorClientes:

    def __init__(self, persist, logger):
        self.clientes: list[Cliente] = []
        self.persist = persist
        self.logger = logger

    def add_cliente(self, cliente: Cliente):

        if not isinstance(cliente, Cliente):
            self.logger.log_error("El objeto proporcionado no es una instancia de Cliente.")
            raise ValueError("El objeto proporcionado no es una instancia de Cliente.")
        
        if not Validate.validate_email(cliente.email):
            self.logger.log_error("Email invalido")
            raise EmailInvalidError("Email inválido")
        
        if not Validate.validate_phone(cliente.phone):
            self.logger.log_error("Telefono invalido")
            raise PhoneInvalidError("Teléfono inválido")
        
        self.clientes.append(cliente)
        self.logger.log_info(f"Cliente con ID {cliente.id} agregado exitosamente.")
        return True
    
    def update_cliente(self, cliente_id: int):
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                print(f"""
================================
== ¿Qué dato desea modificar? ==
================================
                      
[1] Nombre: {cliente.name}
[2] Email: {cliente.email}
[3] Teléfono: {cliente.phone}

                """)
                try:
                    opt = int(input("Ingrese una opción: "))

                    if opt == 1:
                        print("")
                        res = "Nombre"
                        mod = input("Ingresar nuevo nombre: ")
                        cliente.name = mod
                    elif opt == 2:
                        print("")
                        res = "Email"
                        mod = input("Ingresar nuevo email: ")

                        if not Validate.validate_email(mod):
                            raise EmailInvalidError("Email inválido")
                        
                        cliente.email = mod
                    elif opt == 3:
                        print("")
                        res = "Teléfono"
                        mod = input("Ingresar nuevo teléfono: ")

                        if not Validate.validate_phone(mod):
                            raise PhoneInvalidError("Teléfono inválido")
                    
                        cliente.phone = mod
                    else:
                        print("")
                        print("Opción inválida")
                        input("Presione una tecla para continuar...")
                        return False
                    
                    self.save()

                    self.logger.log_info(f"Cliente {cliente_id} actualiza {res} con exito")
                    print("Cliente actualizado correctamente")
                    input("Presione una tecla para continuar...")

                    return True

                except ValueError:
                    print("Opción inválida")
                    input("Presione una tecla para continuar...")
                    continue

                except EmailInvalidError as e:
                    print(f"[ERROR] {e}")
                    print("== NO SE ACTUALIZO EL EMAIL CLIENTE ==")
                    input("Presione una tecla para continuar...")

                except PhoneInvalidError as e:
                    print(f"[ERROR] {e}")
                    print("== NO SE ACTUALIZO EL TELÉFONO CLIENTE ==")
                    input("Presione una tecla para continuar...")

    def del_cliente(self, cliente_id: int):
        encontrado = False
        
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                self.clientes.remove(cliente)
                encontrado = True
                break
        
        if not encontrado:
                print("No existe el ID")
                input("Presione una tecla para continuar...")
                self.logger.log_error(f"Cliente ID {cliente_id} no encontrado")
                return
        
        self.logger.log_info(f"Cliente eliminado: {cliente_id}")

    def list_clientes(self):
        return self.clientes
    
    def save(self):
        data = []

        for cliente in self.clientes:
            data.append(cliente.save_cliente())

        self.persist.save(data)
        self.logger.log_info("Clientes guardados")

    def load(self):
        data = self.persist.load()
        self.clientes = []

        for item in data:

            tipo = item.get("type")

            if tipo == "ClienteRegular":
                cliente = ClienteRegular(
                    item["id"],
                    item["name"],
                    item["email"],
                    item["phone"],
                    item.get("discount", 0)
                )

            elif tipo == "ClientePremium":
                cliente = ClientePremium(
                    item["id"],
                    item["name"],
                    item["email"],
                    item["phone"],
                    item.get("points",0)
                )

            elif tipo == "ClienteCorporativo":
                cliente = ClienteCorporativo(
                    item["id"],
                    item["name"],
                    item["email"],
                    item["phone"],
                    item.get("company",'none')
                )

            else:
                continue

            self.clientes.append(cliente)

        self.logger.log_info("Clientes cargados")
        return data