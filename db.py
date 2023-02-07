# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    db.py                                                ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/02/07 12:07:05 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/07 15:26:36 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import psycopg2
import psycopg2.extras

class DB:
    def __init__(self, dbname: str, user: str, passw: str, host: str, port: int):
        self.conx = psycopg2.connect(
            f"host={host} dbname={dbname} user={user} password={passw} port={port}"
        )

    def close(self) -> None:
        if self.conx is not None:
            self.conx.close()

    def cursor(self):
        return self.conx.cursor()
