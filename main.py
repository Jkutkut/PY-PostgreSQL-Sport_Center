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
#    Updated: 2023/02/11 19:16:03 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from tui.sport_center_tui import SportCenterTUI
from psycopg2 import OperationalError


if __name__ == "__main__":
    print("Initializing app...")
    try:
        program = SportCenterTUI()
        program.run()
        print("Thank you for using the app")
    except OperationalError as e:
        print(e)
