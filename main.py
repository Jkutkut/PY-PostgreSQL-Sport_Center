# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    main.py                                              ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/02/07 09:56:50 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/07 16:49:07 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from TUI.sportCenterTUI import SportCenterTUI
from psycopg2 import OperationalError


if __name__ == "__main__":
    print("Initializing app...")
    try:
        program = SportCenterTUI()
        program.run()
        print("Thank you for using the app")
    except OperationalError as e:
        print(e)
