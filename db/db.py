# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    db.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jre-gonz <jre-gonz@student.42madrid.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: Invalid date        by                   #+#    #+#              #
#    Updated: 2023/02/11 17:39:04 by jre-gonz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

    def execute(self, cx, query: str, args: tuple = tuple()) -> int | None:
        r = cx.execute(query, args)
        self.conx.commit()
        return r

    def getAll(self, cx, query: str, args: tuple = tuple()) -> tuple[any]:
        self.execute(cx, query, args)
        return cx.fetchall()

