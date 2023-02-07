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
#    Updated: 2023/02/07 12:07:28 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import pscopg2
import pscopg2.extras

from db import DB

class SportCenter(DB):
    def __init__(self, user: str, passw: str, host: str, port: int):
        DB.__init__("postgres", user, passw, host, port)
