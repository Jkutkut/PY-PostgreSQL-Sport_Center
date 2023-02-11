# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    sport_center_tui.py                                  ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/02/07 11:51:59 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/11 20:48:17 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from tui.tui import TUI
from db.sport_center_db import SportCenterDB
from model.client import Client

class SportCenterTUI(TUI):
    def __init__(self):
        TUI.__init__(
            self,
            [
                TUI.newOption("Add client", self.ft_addclient),
                TUI.newOption("Remove client", self.ft_removeclient),
                TUI.newOption("Show clients", self.ft_showclients),
                TUI.newOption("Enroll client into a sport", self.ft_registerclientintosport),
                TUI.newOption("Remove client from sport", self.ft_removeclientfromsport),
                TUI.newOption("Show details of client", self.ft_showdetails)
            ]
        )
        self.db = SportCenterDB.init_from_dotenv()
        print("App ready")

    def run(self) -> None:
        TUI.run(self)
        self.db.close()

    def askClientDNI(self) -> str | None:
        dnis = self.db.getClientsDNI()
        if type(dnis) == str:
            print(dnis)
            return None
        if len(dnis) == 0:
            print("There are no clients.")
            return None
        print("Enter the DNI of the client:")
        while True:
            dni = self.askRegex("- DNI: ", Client.VALID_DNI_REGEX)
            if dni in dnis:
                return dni
            print("Client not found.")

    def askSport(self) -> str | None:
        sports = self.db.getSportsNames()
        if type(sports) == str:
            print(sports)
            return None
        if len(sports) == 0:
            print("There are no sports!!")
            return None
        print("Enter the sport:")
        while True:
            sport = self.ask("- Sport: ")
            if sport in sports:
                return sport
            print("Sport invalid.\nValid sports:", ", ".join(sports))

    # ********* ACTIONS *********

    def ft_addclient(self):
        print("Enter the data of the client:")
        r = self.db.addClient(
            Client(
                self.ask(" - Name: ", minlen = 3),
                self.askRegex(" - DNI: ", Client.VALID_DNI_REGEX),
                self.askRegex(" - Birth [yyyy-mm-dd]: ", Client.VALID_BIRTH_REGEX),
                self.askRegex(" - Phone: ", Client.VALID_PHONE_REGEX)
            )
        )
        print(r)

    def ft_removeclient(self):
        print("Enter the data of the client:")
        dni = self.askClientDNI()
        if not dni:
            return
        r = self.db.removeClient(dni)
        print(r)

    def ft_showclients(self):
        r = self.db.getAllClients()
        print(r)

    def ft_registerclientintosport(self):
        dni = self.askClientDNI()
        if not dni:
            return
        sport = self.askSport()
        if not sport:
            return
        r = self.db.addEnrollment(
            dni,
            sport,
            self.ask("- Schedule: "),
            check_args = False
        )
        print(r)

    def ft_removeclientfromsport(self):
        dni = self.askClientDNI()
        if not dni:
            return
        sports = self.db.getClientSports(dni)
        if type(sports) == str:
            print(sports)
            return
        sport = self.askOptionNoCase("- Select the sport: ", sports)
        r = self.db.removeEnrollment(dni, sport)
        print(r)

    def ft_showdetails(self):
        dni = self.askClientDNI()
        if not dni:
            return
        r = self.db.getClientDetails(dni, check_dni = False)
        print(r)
