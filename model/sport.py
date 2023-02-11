# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    sport.py                                             ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/02/11 18:06:11 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/11 18:06:13 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from model.postgresql_model import PostgreSQLModel

class Sport(PostgreSQLModel):
    __TABLE_NAME__ = "DEPORTES"
    NAME           = "nombre"
    PRICE          = "precio"

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price
