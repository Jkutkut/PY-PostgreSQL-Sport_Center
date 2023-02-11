from model.postgresql_model import PostgreSQLModel

class Sport(PostgreSQLModel):
    __TABLE_NAME__ = "DEPORTES"
    NAME           = "nombre"
    PRICE          = "precio"

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price