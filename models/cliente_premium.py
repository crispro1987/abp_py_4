from models.cliente import Cliente

class ClientePremium(Cliente):
    def __init__(self, id, name, email, phone, points: int):
        super().__init__(id, name, email, phone)
        self._points = points

    # Getter
    @property
    def points(self):
        return self._points
    
    # Setter
    @points.setter
    def points(self, value: int):
        if value < 0:
            raise ValueError("Los puntos no pueden ser menor a 0")
        self._points = value

    def type_cliente(self):
        return super().type_cliente() + " Premium"
    
    def save_cliente(self):
        data = super().save_cliente()
        data["points"] = self.points
        return data