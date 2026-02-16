class Validate:

    # Validar que email contenga @ y un punto.

    @staticmethod
    def validate_email(email: str):
        return "@" in email and "." in email
    
    # Validar que teléfono sean numeros y la cantidad sea igual a 8

    @staticmethod
    def validate_phone(phone: str):
        return phone.isdigit() and len(phone) == 8