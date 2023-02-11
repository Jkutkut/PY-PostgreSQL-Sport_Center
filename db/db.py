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
#    Created: 2023/02/11 18:08:45 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/11 18:29:56 by Jkutkut            '-----------------'    #
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

    def execute_file(self, cx, filename) -> None:
        print(f"Executing script: {filename}:")
        with open(filename) as f:
            for line in f:
                line = line
                if line == "\n" or line[0] == "-":
                    continue
                print(".", end="")
                cx.execute(line)
        self.conx.commit()
        print(" Done!")

    def execute(self, cx, query: str, args: tuple = tuple()) -> None:
        cx.execute(query, args)
        self.conx.commit()

    def getAll(self, cx, query: str, args: tuple = tuple()) -> tuple[any]:
        self.execute(cx, query, args)
        return cx.fetchall()

