from models.cliente import Cliente

class ClientePremium(Cliente):
    def __init__(self, id, name, email, phone, points: int):
        super().__init__(id, name, email, phone)
        self.points = points
    
    def type_cliente(self):
        return super().type_cliente() + " Premium"
    
    def save_cliente(self):
        data = super().save_cliente()
        data["points"] = self.points
        return data