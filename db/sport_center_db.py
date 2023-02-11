# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    sport_center_db.py                                   ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/02/11 18:07:11 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/11 22:05:03 by Jkutkut            '-----------------'    #
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
        self.cursor = None
        try:
            self.cursor = self.new_cursor()
            self.init_db()
        except:
            self.close()
            raise Exception("There was an error with the DB")

    def close(self) -> None:
        if self.cursor is not None:
            self.cursor.close()
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
        self.cursor.execute(
            """SELECT EXISTS(
                SELECT * FROM information_schema.tables where lower(table_name) = lower(%s)
            )""",
            [Client.__TABLE_NAME__]
        )
        db_exists = self.cursor.fetchone()[0]
        if not db_exists:
            self.execute_file(self.cursor, self.CONFIG_FILE)

    # ********* ACTIONS *********

    def addClient(self, c: Client) -> str:
        query = f"INSERT INTO {Client.TABLE_NAME()} VALUES (%s, %s, %s, %s);"
        try:
            self.execute(
                self.cursor,
                query,
                (c.name, c.dni, c.birth, c.phone)
            )
            r = "Client added correctly."
        except UniqueViolation as e:
            r = "Ups, the DNI is not valid."
        except:
            r = "There was an error with the DB."
        return r

    def removeClient(self, dni: str) -> str:
        query = f"DELETE FROM {Client.TABLE_NAME()} WHERE {Client.DNI} = %s;"
        try:
            self.execute(
                self.cursor,
                query,
                tuple([dni])
            )
            r = "Client removed correctly."
        except:
            r = "There was an error with the DB."
        return r

    def getAllClients(self) -> str:
        query = f"SELECT * FROM {Client.TABLE_NAME()};"
        try:
            sql_result = self.getAll(self.cursor, query)
            r = "\n".join([Client(*e).__datos__() for e in sql_result])
            r = "List of all the clients:\n\n" + r
        except:
            r = "There was an error with the DB."
        return r

    def addEnrollment(self, dni: str, sport: str, schedule: str, check_args: bool = True) -> str:
        if check_args:
            client = self.getClient(dni)
            if not client:
                return "Invalid DNI. Are you sure it is right?"
            elif type(client) == str:
                return client
            sport_obj = self.getSport(sport)
            if not sport:
                return "Invalid sport. Are you sure it is right?"
            elif type(sport_obj) == str:
                return sport_obj
        query = f"INSERT INTO {SportEnrollment.TABLE_NAME()} VALUES (%s, %s, %s);"
        try:
            self.execute(self.cursor, query, (dni, sport, schedule))
            r = "Enrollment added successfully."
        except UniqueViolation as e:
            r = "This client is already enrolled."
        except:
            r = "There was an error with the DB" # TODO refactor into constant
        return r

    def removeEnrollment(self, dni: str, sport: str) -> str:
        query = f"""
            DELETE FROM {SportEnrollment.TABLE_NAME()}
            WHERE
                {SportEnrollment.CLIENT_ID} = %s and
                {SportEnrollment.SPORT_ID} = %s;"""
        try:
            self.execute(
                self.cursor,
                query,
                (dni, sport)
            )
            r = "Enrollment removed"
        except:
            r = "There was an error with the DB"
        return r


    def getClientDetails(self, dni: str, check_dni: bool = True) -> str:
        if check_dni:
            client = self.getClient(dni)
            if not client:
                return "Invalid DNI. Are you sure it is right?"
            elif type(client) == str:
                return client
        query = f"""
            SELECT d.{Sport.NAME}, d.{Sport.PRICE}, m.{SportEnrollment.PERIOD}
            FROM {Sport.TABLE_NAME()} as d, {SportEnrollment.TABLE_NAME()} as m
            WHERE m.{SportEnrollment.CLIENT_ID} = %s and m.{SportEnrollment.SPORT_ID} like d.{Sport.NAME};"""
        try:
            d = self.getAll(self.cursor, query, [dni])
            if len(d) == 0:
                r = "This client is not in any sports at the moment."
            else:
                enrollments = [SportEnrollment(Sport(*e[:-1]), e[-1]) for e in d]
                r = "List of all the sports enrolled in:\n"
                r += Client.__deportes__(enrollments)
        except:
            r = "There was an error with the DB."
        return r

    # ********* DB Get *********

    def getClient(self, dni: str) -> Client | str | None:
        query = f"SELECT * from {Client.TABLE_NAME()} WHERE {Client.DNI} = %s;"
        try:
            self.execute(self.cursor, query, [dni])
            client = self.cursor.fetchone()
            if client is not None:
                client = Client(*client)
            return client
        except:
            return "There was an error with the DB."

    def getClientsDNI(self) -> list[str] | str:
        query = f"SELECT {Client.DNI} from {Client.TABLE_NAME()};"
        try:
            return [e[0] for e in self.getAll(self.cursor, query)]
        except:
            return "There was an error with the DB."

    def getClientSports(self, dni: str) -> list[str] | str:
        query = f"""
            SELECT {SportEnrollment.SPORT_ID}
            FROM {SportEnrollment.TABLE_NAME()}
            WHERE {SportEnrollment.CLIENT_ID} = %s;"""
        try:
            return [s[0] for s in self.getAll(self.cursor, query, [dni])]
        except Exception as e:
            print(e)
            return "There was an error with the DB."

    def getSport(self, sport: str) -> Sport | str | None:
        query = f"SELECT * from {Sport.TABLE_NAME()} WHERE {Sport.NAME} = %s;"
        try:
            self.execute(self.cursor, query, [sport])
            sport_obj = self.cursor.fetchone()
            if sport_obj is not None:
                sport_obj = Sport(*sport_obj)
            return sport_obj
        except:
            return "There was an error with the DB."

    def getSportsNames(self) -> list[str] | str:
        query = f"SELECT {Sport.NAME} from {Sport.TABLE_NAME()};"
        try:
            return [e[0] for e in self.getAll(self.cursor, query)]
        except:
            return "There was an error with the DB."

# TODO syntax check
# TODO Change tui text' options
# TODO case sensitivity
# TODO commit only if DB changed
