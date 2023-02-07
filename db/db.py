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
#    Updated: 2023/02/07 19:02:23 by Jkutkut            '-----------------'    #
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
