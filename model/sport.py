class Sport:
    TABLE_NAME = "DEPORTES"
    NAME       = "nombre"
    PRICE      = "precio"

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price