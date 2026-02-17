# Sistema Gestión Inteligente de Clientes (GIC)
## Proyecto Módulo #4 | ABP



## Tecnologías utilizadas

- Python 3.14
- Github

## Estructura del proyecto

```
abp_py_4/
│
├── data/
│   ├── clientes.json
│   └── logs.txt
├── gestor/
│   └── gestor_clientes.py
├── models/
│   ├── cliente_corporativo.py
│   ├── cliente_premium.py
│   ├── cliente_regular.py
|   └── cliente.py
├── persist/
|   └── persist.py
├── utils/
│   ├── exceptions.py
│   ├── functions.py
│   ├── logger.py
|   └── validate.py
├── main.py
├── README.md
└── uml.xml
```

## Ejecutar Sistema

Clonar repositorio

```
git clone "https://github.com/crispro1987/abp_py_4.git"
```

Ejecutar

```
cd abp_py_4

python main.py
```

## Modelo UML

![UML](https://www.dosiscl.com/abp4.webp)

## Herencia

La herencia la podemos ver en las clases hijas (ClienteRegular, ClientePremium y ClienteCorporativo) extienden la funcionalidad de la clase Cliente

```
class Cliente:
    def __init__(self, id:int, name:str, email:str, phone: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

class ClienteRegular(Cliente):
    def __init__(self, id, name, email, phone, discount: float):
        super().__init__(id, name, email, phone)
        self._discount = discount
```


## Polimorfismo

Se aplica cuando varias clases tienen el mismo metodo pero se comportan de manera diferente

```
# Clase cliente

def type_cliente(self):
        return "Cliente"

# Clase cliente regular

def type_cliente(self):
        return super().type_cliente() + " Regular"

```


## Encapsulación

La encapsulación al definir atributos "privados" protegidos. Controlando el acceso con Getters y Setters.

```
# Getter
@property
def discount(self):
    return self._discount
    
# Setter
@discount.setter
def discount(self, value: float):
    if value < 0:
        raise ValueError("El descuento no puede ser menor a 0")
    self._discount = value

```

## Validaciones

Las validaciones estan centralizadas en una clase (Validate), lo que hace que este codigo sea mantenible y reutilizable.

```
class Validate:

    # Validar que email contenga @ y un punto.

    @staticmethod
    def validate_email(email: str):
        return "@" in email and "." in email
    
    # Validar que teléfono sean numeros y la cantidad sea igual a 8

    @staticmethod
    def validate_phone(phone: str):
        return phone.isdigit() and len(phone) == 8

```

## Manejo de errores estructurado

Manejo de errores mediante excepciones personalizadas (try-except) con errores especificos cuando las validaciones fallan.

```
try:

    #... código ...

    if not Validate.validate_email(mod):
        raise EmailInvalidError("Email inválido")

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

```


## Persistencia JSON

La persistencia se crea con el metodo save()

```
open(self.file, "w")
```
Abre el archivo en modo escritura (w) y si no existe lo crea. Si existe lo sobrescribe

```
with ... as f
```
Maneja el archivo y lo cierra al terminar

```
json.dump(data, f, indent=4)
```
Convierte data a formato JSON y lo escribe en el archivo.
__indent=4__ hace que el JSON sea legible


## Gestión de clientes

El gestor de clientes es el cerebro del sistema. La función principal es centralizar la lógica de negocio

## Registro de actividad

El Logger escribe los logs con distintos niveles (INFO y ERROR)

con el metodo privado _write

```
def _write(self, level: str, msg: str):
```

este metodo se encarga de escribir el archivo y funciona casi igual que la persistencia solo que aca en el logger lo que hace es agregar el log al final del archivo sin reemplazar

```
with open(self.file, "a") as f:
```
