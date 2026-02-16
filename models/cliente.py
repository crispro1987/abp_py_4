class Cliente:
    def __init__(self, id:int, name:str, email:str, phone: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        

    def type_cliente(self):
        return "Cliente"
    

    def save_cliente(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "type": self.__class__.__name__
        } 
    
    def __str__(self):
        return f"[ID]: {self.id}, [Nombre]: {self.name}, [Email]: {self.email}, [Teléfono]: {self.phone}, [Tipo de Cliente]: {self.type_cliente()}"
    
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.id == other.id
        return False