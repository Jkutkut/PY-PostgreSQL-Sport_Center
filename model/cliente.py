class Cliente:

    NOMBRE = "nombre"
    DNI = "dni"
    FNAC = "fnac"
    TEL = "telefono"

    def __init__(self, nombre, dni, fnac, tel):
        self.nombre = nombre
        self.dni = dni
        self.fnac = fnac
        self.tel = tel

    def __deportes__(self, cx) -> None:
        # TODO
        pass

    def __datos__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"Cliente {self.nombre}\n - DNI: {self.dni}\n - Birth: {self.fnac}\n - Phone: {self.tel}\n"


