from models.cliente import Cliente

class ClienteRegular(Cliente):
    def __init__(self, id, name, email, phone, discount: float):
        super().__init__(id, name, email, phone)
        self.discount = discount

    def type_cliente(self):
        return super().type_cliente() + " Regular"
    
    def save_cliente(self):
        data = super().save_cliente()
        data["discount"] = self.discount
        return data