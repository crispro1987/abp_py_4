from models.cliente import Cliente

class ClienteRegular(Cliente):
    def __init__(self, id, name, email, phone, discount: float):
        super().__init__(id, name, email, phone)
        self._discount = discount

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

    def type_cliente(self):
        return super().type_cliente() + " Regular"
    
    def save_cliente(self):
        data = super().save_cliente()
        data["discount"] = self.discount
        return data