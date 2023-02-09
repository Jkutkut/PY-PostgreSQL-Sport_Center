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
#    Updated: 2023/02/09 12:59:28 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import os
import dotenv
from psycopg2.errors import UniqueViolation

from db.db import DB
from model.client import Client

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
        if not db_exists:
            self.execute_file(cx, self.CONFIG_FILE)
        cx.close()

    def addClient(self, c: Client) -> str:
        print(f"Adding: {c}")
        cx = self.cursor()
        query = "INSERT INTO public.\"CLIENTES\" VALUES (%s, %s, %s, %s);"
        try:
            self.execute(
                cx,
                query,
                (
                    c.name,
                    c.dni,
                    c.birth,
                    c.phone
                )
            )
            print("Client added correctly.")
        except UniqueViolation as e:
            print(f"Can not insert the client: {e}")
        except Exception as e:
            print(e)
            print(e.__class__.__name__)
            e.__str__() # TODO
        cx.close()
