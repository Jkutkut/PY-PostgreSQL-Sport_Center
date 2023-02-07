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
#    Updated: 2023/02/07 13:52:42 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from sportCenterTUI import SportCenterTUI

if __name__ == "__main__":
    print("Initializing app...")
    program = SportCenterTUI()
    program.run()
    print("Thank you for using the app")
