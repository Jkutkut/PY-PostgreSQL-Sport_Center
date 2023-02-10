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
#    Updated: 2023/02/10 13:06:54 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from TUI.tui import TUI
from db.sportCenterDB import SportCenterDB
from model.client import Client

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
        print("App ready")

    def run(self) -> None:
        TUI.run(self)
        self.db.close()

    def ft_addclient(self):
        print("Enter the data of the client:")
        r = self.db.addClient(
            Client(
                self.ask(" - Name: ", minlen = 3),
                self.askRegex(" - DNI: ", Client.VALID_DNI_REGEX),
                self.askRegex(" - Birth [yyyy-mm-dd]: ", Client.VALID_BIRTH_REGEX),
                self.askRegex(" - Phone: ", Client.VALID_PHONE_REGEX)
            )
            # Client("Pepe", "98765432A", "1990-12-30", "432 432 123")
        )
        print(r)

    def ft_removeclient(self):
        print("Enter the data of the client:")
        r = self.db.removeClient(
            self.askRegex(" - DNI: ", Client.VALID_DNI_REGEX)
        )
        print(r)

    def ft_showclients(self):
        r = self.db.getAllClients()
        print(r)

    def ft_registerclientintosport(self):
        print("TODO")

    def ft_removeclientfromsport(self):
        print("TODO")

    def ft_showdetails(self):
        print("TODO")
