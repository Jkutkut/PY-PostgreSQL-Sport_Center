# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    sportCenterDB.py                                     ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/02/07 12:07:26 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/07 13:51:17 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import os
import dotenv

from db import DB

class SportCenterDB(DB):
    def __init__(self, user: str, passw: str, host: str, port: int):
        DB.__init__(self, "postgres", user, passw, host, port)
        print("DB created :D")

    @staticmethod
    def initfrom_dotenv():
        dotenv.load_dotenv()
        return SportCenterDB(
            os.getenv("DB_USR"),
            os.getenv("DB_USR_PASSWD"),
            "localhost",
            os.getenv("DB_PORT")
        )
