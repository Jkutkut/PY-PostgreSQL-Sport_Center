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
#    Updated: 2023/02/11 23:48:15 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from tui.tui import TUI
from db.sport_center_db import SportCenterDB
from model.client import Client

class SportCenterTUI(TUI):
    def __init__(self) -> None:
        TUI.__init__(
            self,
            [
                TUI.new_option("Add client", self.ft_add_client),
                TUI.new_option("Remove client", self.ft_remove_client),
                TUI.new_option("Show clients", self.ft_show_clients),
                TUI.new_option("Enroll client into a sport", self.ft_register_client_into_sport),
                TUI.new_option("Remove client from sport", self.ft_remove_client_from_sport),
                TUI.new_option("Show details of client", self.ft_show_details)
            ]
        )
        self.db: SportCenterDB = SportCenterDB.init_from_dotenv()
        print("App ready.")

    def run(self) -> None:
        TUI.run(self)
        self.db.close()

    def ask_client_dni(self) -> str | None:
        dnis: list[str] | str = self.db.get_clients_dni()
        if type(dnis) == str:
            print(dnis)
            return None
        elif len(dnis) == 0:
            print("There are no clients.")
            return None
        print("Enter the DNI of the client:")
        while True:
            dni: str = self.ask_regex("- DNI: ", Client.VALID_DNI_REGEX).upper()
            if dni in dnis:
                return dni
            print("Client not found.")

    def ask_sport(self) -> str | None:
        sports: list[str] | str = self.db.get_sports_names()
        if type(sports) == str:
            print(sports)
            return None
        if len(sports) == 0:
            print("There are no sports!")
            return None
        print("Enter the sport:")
        while True:
            sport: str = self.ask("- Sport: ").lower()
            if sport in sports:
                return sport
            print("Sport invalid.\nValid sports:", ", ".join(sports))

    # ********* ACTIONS *********

    def ft_add_client(self) -> None:
        print("Enter the data of the client:")
        r: str = self.db.add_client(
            Client(
                self.ask(" - Name: ", minlen = 3),
                self.ask_regex(" - DNI: ", Client.VALID_DNI_REGEX),
                self.ask_regex(" - Birth [yyyy-mm-dd]: ", Client.VALID_BIRTH_REGEX),
                self.ask_regex(" - Phone: ", Client.VALID_PHONE_REGEX)
            )
        )
        print(r)

    def ft_remove_client(self) -> None:
        print("Enter the data of the client:")
        dni: str | None = self.ask_client_dni()
        if not dni:
            return
        r: str = self.db.remove_client(dni)
        print(r)

    def ft_show_clients(self) -> None:
        r: str = self.db.get_all_clients()
        print(r)

    def ft_register_client_into_sport(self) -> None:
        dni: str | None = self.ask_client_dni()
        if not dni:
            return
        sport: str | None = self.ask_sport()
        if not sport:
            return
        r: str = self.db.add_enrollment(
            dni,
            sport,
            self.ask("- Schedule: "),
            check_args = False
        )
        print(r)

    def ft_remove_client_from_sport(self) -> None:
        dni: str | None = self.ask_client_dni()
        if not dni:
            return
        sports: str | None = self.db.get_client_sports(dni)
        if type(sports) == str:
            print(sports)
            return
        sport: str = self.ask_option_no_case("- Select the sport: ", sports)
        r: str = self.db.remove_enrollment(dni, sport)
        print(r)

    def ft_show_details(self) -> None:
        dni: str | None = self.ask_client_dni()
        if not dni:
            return
        r: str = self.db.get_client_details(dni, check_dni = False)
        print(r)
