from models.cliente import Cliente

class ClienteCorporativo(Cliente):
    def __init__(self, id, name, email, phone, company: str):
        super().__init__(id, name, email, phone)
        self.company = company

    def type_cliente(self):
        return super().type_cliente() + " Corporativo"
    
    def save_cliente(self):
        data = super().save_cliente()
        data["company"] = self.company
        return data