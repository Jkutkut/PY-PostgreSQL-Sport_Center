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
#    Updated: 2023/02/11 23:47:56 by Jkutkut            '-----------------'    #
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

    def __init__(self, user: str, passw: str, host: str, port: int) -> None:
        DB.__init__(self, "postgres", user, passw, host, port)
        self.cursor = None
        try:
            self.cursor = self.new_cursor()
            self.init_db()
        except:
            self.close()
            raise Exception(self.DB_ERROR_MSG)

    def close(self) -> None:
        if self.cursor is not None:
            self.cursor.close()
        DB.close(self)

    @classmethod
    def init_from_dotenv(cls) -> any:
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
        db_exists: bool = self.cursor.fetchone()[0]
        if not db_exists:
            self.execute_file(self.cursor, self.CONFIG_FILE)

    # ********* ACTIONS *********

    def add_client(self, c: Client) -> str:
        query: str = f"INSERT INTO {Client.TABLE_NAME()} VALUES (%s, %s, %s, %s);"
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
            r = self.DB_ERROR_MSG
        return r

    def remove_client(self, dni: str) -> str:
        query: str = f"DELETE FROM {Client.TABLE_NAME()} WHERE {Client.DNI} = %s;"
        try:
            self.execute(
                self.cursor,
                query,
                tuple([dni])
            )
            r = "Client removed correctly."
        except:
            r = self.DB_ERROR_MSG
        return r

    def get_all_clients(self) -> str:
        query: str = f"SELECT * FROM {Client.TABLE_NAME()};"
        try:
            sql_result = self.get_all(self.cursor, query)
            r = "\n".join([Client(*e).__datos__() for e in sql_result])
            r = "List of all the clients:\n\n" + r
        except:
            r = self.DB_ERROR_MSG
        return r

    def add_enrollment(self, dni: str, sport: str, schedule: str, check_args: bool = True) -> str:
        if check_args:
            client: Client | str | None = self.get_client(dni)
            if not client:
                return "Invalid DNI. Are you sure it is right?"
            elif type(client) == str:
                return client
            sport_obj: Sport | str | None = self.get_sport(sport)
            if not sport:
                return "Invalid sport. Are you sure it is right?"
            elif type(sport_obj) == str:
                return sport_obj
        query: str = f"INSERT INTO {SportEnrollment.TABLE_NAME()} VALUES (%s, %s, %s);"
        try:
            self.execute(self.cursor, query, (dni, sport, schedule))
            r = "Enrollment added successfully."
        except UniqueViolation as e:
            r = "This client is already enrolled."
        except:
            r = self.DB_ERROR_MSG
        return r

    def remove_enrollment(self, dni: str, sport: str) -> str:
        query: str = f"""
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
            r = "Enrollment removed."
        except:
            r = self.DB_ERROR_MSG
        return r


    def get_client_details(self, dni: str, check_dni: bool = True) -> str:
        if check_dni:
            client: Client | str | None = self.get_client(dni)
            if not client:
                return "Invalid DNI. Are you sure it is right?"
            elif type(client) == str:
                return client
        query: str = f"""
            SELECT d.{Sport.NAME}, d.{Sport.PRICE}, m.{SportEnrollment.PERIOD}
            FROM {Sport.TABLE_NAME()} as d, {SportEnrollment.TABLE_NAME()} as m
            WHERE m.{SportEnrollment.CLIENT_ID} = %s and m.{SportEnrollment.SPORT_ID} like d.{Sport.NAME};"""
        try:
            d: list[tuple[str|int]] = self.get_all(self.cursor, query, [dni])
            if len(d) == 0:
                r = "This client is not in any sports at the moment."
            else:
                enrollments: list[SportEnrollment] = [SportEnrollment(Sport(*e[:-1]), e[-1]) for e in d]
                r = "List of all the sports enrolled in:\n"
                r += Client.__deportes__(enrollments)
        except:
            r = self.DB_ERROR_MSG
        return r

    # ********* DB Get *********

    def get_client(self, dni: str) -> Client | str | None:
        query: str = f"SELECT * from {Client.TABLE_NAME()} WHERE {Client.DNI} = %s;"
        try:
            self.execute(self.cursor, query, [dni], commit = False)
            client: tuple[any] = self.cursor.fetchone()
            if client is not None:
                client: Client = Client(*client)
            return client
        except:
            return self.DB_ERROR_MSG

    def get_clients_dni(self) -> list[str] | str:
        query: str = f"SELECT {Client.DNI} from {Client.TABLE_NAME()};"
        try:
            return [e[0] for e in self.get_all(self.cursor, query)]
        except:
            return self.DB_ERROR_MSG

    def get_client_sports(self, dni: str) -> list[str] | str:
        query = f"""
            SELECT {SportEnrollment.SPORT_ID}
            FROM {SportEnrollment.TABLE_NAME()}
            WHERE {SportEnrollment.CLIENT_ID} = %s;"""
        try:
            return [s[0] for s in self.get_all(self.cursor, query, [dni])]
        except:
            return self.DB_ERROR_MSG

    def get_sport(self, sport: str) -> Sport | str | None:
        query: str = f"SELECT * from {Sport.TABLE_NAME()} WHERE {Sport.NAME} = %s;"
        try:
            self.execute(self.cursor, query, [sport])
            sport_obj: tuple[any] = self.cursor.fetchone()
            if sport_obj is not None:
                sport_obj: Sport = Sport(*sport_obj)
            return sport_obj
        except:
            return self.DB_ERROR_MSG

    def get_sports_names(self) -> list[str] | str:
        query: str = f"SELECT {Sport.NAME} from {Sport.TABLE_NAME()};"
        try:
            return [e[0] for e in self.get_all(self.cursor, query)]
        except:
            return self.DB_ERROR_MSG
