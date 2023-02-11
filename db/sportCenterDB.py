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
#    Created: 2023/02/11 18:07:11 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/11 18:32:06 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import os
import dotenv
from psycopg2.errors import UniqueViolation

from db.db import DB
from model.client import Client
from model.sport import Sport
from model.sport_enrollment import SportEnrollment

class SportCenterDB(DB):

    CONFIG_FILE = "db/.init_script.sql"

    def __init__(self, user: str, passw: str, host: str, port: int):
        DB.__init__(self, "postgres", user, passw, host, port)
        self.init_db()
        self.cg = self.cursor()

    def close(self) -> None:
        self.cg.close()
        DB.close(self)

    @classmethod
    def init_from_dotenv(cls):
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
                SELECT * FROM information_schema.tables where lower(table_name) = lower(%s)
            )""",
            [Client.__TABLE_NAME__]
        )
        db_exists = cx.fetchone()[0]
        if not db_exists:
            self.execute_file(cx, self.CONFIG_FILE)
        cx.close()

    # ********* ACTIONS *********

    def addClient(self, c: Client) -> str:
        cx = self.cursor()
        query = f"INSERT INTO {Client.TABLE_NAME()} VALUES (%s, %s, %s, %s);"
        try:
            self.execute(
                cx,
                query,
                (c.name, c.dni, c.birth, c.phone)
            )
            r = "Client added correctly."
        except UniqueViolation as e:
            r = "Ups, the DNI is not valid."
        except:
            r = "There was an error with the DB."
        cx.close()
        return r

    def removeClient(self, dni: str) -> str:
        cx = self.cursor()
        query = f"DELETE FROM {Client.TABLE_NAME()} WHERE {Client.DNI} = %s;"
        try:
            self.execute(
                cx,
                query,
                tuple([dni])
            )
            r = "Client removed correctly."
        except:
            r = "There was an error with the DB."
        cx.close()
        return r

    def getAllClients(self) -> str:
        cx = self.cursor()
        query = f"SELECT * FROM {Client.TABLE_NAME()};"
        try:
            sql_result = self.getAll(cx, query)
            r = "\n".join([Client(*e).__datos__() for e in sql_result])
            r = "List of all the clients:\n\n" + r
        except:
            r = "There was an error with the DB."
        return r

    def getClientDetails(self, dni: str, check_dni: bool = True) -> str:
        cx = self.cursor()
        if check_dni:
            client = self.getClient(dni)
            if not client:
                return "Invalid DNI. Are you sure it is right?"
            if type(client) == str:
                return client
        query = f"""
            SELECT d.{Sport.NAME}, d.{Sport.PRICE}, m.{SportEnrollment.PERIOD}
            FROM {Sport.TABLE_NAME()} as d, {SportEnrollment.TABLE_NAME()} as m
            WHERE m.{SportEnrollment.CLIENT_ID} = %s and m.{SportEnrollment.SPORT_ID} like d.{Sport.NAME};"""
        try:
            d = self.getAll(cx, query, [dni])
            if len(d) == 0:
                r = "This client is not in any sports at the moment."
            else:
                enrollments = [SportEnrollment(Sport(*e[:-1]), e[-1]) for e in d]
                r = "List of all the sports enrolled in:\n"
                r += Client.__deportes__(enrollments)
        except:
            r = "There was an error with the DB."
        cx.close()
        return r

    # ********* DB Get *********

    def getClient(self, dni: str) -> Client | str | None:
        query = f"SELECT * from {Client.TABLE_NAME()} WHERE {Client.DNI} = %s;"
        try:
            self.execute(self.cg, query, [dni])
            client = self.cg.fetchone()
            if client is not None:
                client = Client(*client)
        except:
            return "There was an error with the DB."
        return client

    def getClientsDNI(self) -> list[str] | str:
        query = f"SELECT DNI from {Client.TABLE_NAME()};"
        try:
            return self.getAll(self.cg, query)
        except:
            return "There was an error with the DB."
