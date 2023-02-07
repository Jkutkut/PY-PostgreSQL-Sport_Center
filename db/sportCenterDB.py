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
#    Updated: 2023/02/07 17:49:29 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import os
import dotenv

from db.db import DB

class SportCenterDB(DB):

    CONFIG_FILE = "db/.init_script.sql"

    def __init__(self, user: str, passw: str, host: str, port: int):
        DB.__init__(self, "postgres", user, passw, host, port)
        self.init_db()

    @staticmethod
    def initfrom_dotenv():
        dotenv.load_dotenv()
        return SportCenterDB(
            os.getenv("DB_USR"),
            os.getenv("DB_USR_PASSWD"),
            "localhost",
            os.getenv("DB_PORT")
        )

    def init_db(self) -> None:
        cx = self.cursor()
        cx.execute(
            """SELECT EXISTS(
                SELECT * FROM information_schema.tables where table_name=%s
            )""",
            ('CLIENTES',)
        )
        db_exists = cx.fetchone()[0]
        if db_exists:
            return
        self.execute_file(cx, self.CONFIG_FILE)
        cx.close()
