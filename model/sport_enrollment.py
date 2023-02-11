# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    sport_enrollment.py                                  ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/02/11 18:06:19 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/11 18:06:21 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from model.postgresql_model import PostgreSQLModel
from model.sport import Sport

class SportEnrollment(PostgreSQLModel):
    __TABLE_NAME__ = "MATRICULAS"
    CLIENT_ID      = "dni"
    SPORT_ID       = "deporte"
    PERIOD         = "horario"

    def __init__(self, sport: Sport, period: str) -> None:
        self.sport = sport
        self.period = period

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.sport.name} {self.period}"
