# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    sportCenterTUI.py                                    ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/02/07 11:51:59 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/07 13:54:07 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from tui import TUI
from sportCenterDB import SportCenterDB

class SportCenterTUI(TUI):
    def __init__(self):
        TUI.__init__(
            self,
            [
                TUI.newOption("Add client", self.ft_addclient),
                TUI.newOption("Remove client", self.ft_removeclient),
                TUI.newOption("Show clients", self.ft_showclients),
                TUI.newOption("Add client to sport", self.ft_registerclientintosport),
                TUI.newOption("Remove client from sport", self.ft_removeclientfromsport),
                TUI.newOption("Show details of client", self.ft_showdetails)
            ]
        )
        self.db = SportCenterDB.initfrom_dotenv()

    def run(self) -> None:
        TUI.run(self)
        self.db.close()

    def ft_addclient(self):
        print("TODO")

    def ft_removeclient(self):
        print("TODO")

    def ft_showclients(self):
        print("TODO")

    def ft_registerclientintosport(self):
        print("TODO")

    def ft_removeclientfromsport(self):
        print("TODO")

    def ft_showdetails(self):
        print("TODO")
