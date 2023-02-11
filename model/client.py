from model.sport_enrollment import SportEnrollment

class Client:
    TABLE_NAME = "CLIENTES"
    NAME       = "nombre"
    DNI        = "dni"
    BIRTH      = "fnac"
    PHONE      = "telefono"

    # https://github.com/jkutkut/regex
    VALID_DNI_REGEX = r'^[0-9]{8}[A-Z]$'
    VALID_BIRTH_REGEX = r'^(?:(?:(?:(?:(?:[13579][26]|[2468][048])00)|(?:[0-9]{2}(?:(?:[13579][26])|(?:[2468][048]|0[48]))))-(?:02-(?:0[1-9]|1[0-9]|2[0-8])))|(?:(?:[0-9]{4}-(?:(?:(?:0[13578]|1[02])-(?:0[1-9]|[12][0-9]|3[01]))|(?:(?:0[469]|11)-(?:0[1-9]|[12][0-9]|30))|(?:02-(?:0[1-9]|[1][0-9]|2[0-9]))))))$'
    VALID_PHONE_REGEX = r'^(\+\d{2,3})? ?\d{3} ?(\d{3} ?\d{3}|\d{2} ?\d{2} ?\d{2})$'

    def __init__(self, name: str, dni: str, birth: str, phone: str) -> None:
        self.name = name
        self.dni = dni
        self.birth = birth
        self.phone = phone

    @staticmethod
    def __deportes__(sports: list[SportEnrollment]) -> str:
        if len(sports) == 0:
            return "No sports enrolled."
        r: str = ""
        for enrollment in sports:
            r += f" - {enrollment.sport.name}, {enrollment.period} schedule ({enrollment.sport.price} €/month)\n"
        return r

    def __datos__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.name}\n - DNI: {self.dni}\n - Birth: {self.birth}\n - Phone: {self.phone}\n"


