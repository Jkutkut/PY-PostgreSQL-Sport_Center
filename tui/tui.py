# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    tui.py                                               ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/02/07 11:52:04 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/11 23:24:29 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import re

class TUI:
    def __init__(self, options: dict) -> None:
        self.running: bool = True
        self.options: dict = options
        self.options.append(TUI.new_option("exit", self.exit))

    def new_option(name: str, ft) -> dict:
        return {"name": name, "ft": ft}

    def run(self) -> None:
        if not self.running:
            raise Exception("Execution ended")
        while self.running:
            r: str = self.ask_options(self.options)
            self.options[r]["ft"]()

    def ask(self, question: str, minlen: int = -1, maxlen: int = -1) -> str:
        while True:
            r = input(question).strip()
            print()
            if maxlen > 0 and len(r) > maxlen:
                print("The length of the response is too long. Use {maxlen} chars at max.")
                continue
            if minlen > 0 and len(r) < minlen:
                print("The length of the response is not long enough.")
                continue
            return r

    def ask_options(self, options: dict) -> int:
        opts: list[str] = [f"{i + 1}: {options[i]['name']}" for i in range(len(options))]
        opts: str = "\nWhat do you want to do?\n" + "\n".join(opts) + "\n-> "
        while True:
            try:
                inp: str = self.ask(opts)
                if len(inp) == 0:
                    continue
                idx: int = int(inp) - 1
                if idx < 0 or idx >= len(options):
                    print(f"Invalid number: It should be in the range [1, {len(options)}].")
                else:
                    return idx
            except ValueError:
                print("Invalid number")

    def ask_option_no_case(self, question: str, options: list[str]) -> str:
        question: str = question + " [" + "|".join(options) + "]\n-> "
        options: list[str] = [o.lower() for o in options]
        while True:
            option: str = self.ask(question).lower()
            for o in options:
                if o.lower() == option:
                    return o
            print("Please, select one of the options. Avaliable:", ", ".join(options))

    def ask_regex(self, question: str, regex: str) -> str:
        while True:
            option: str = self.ask(question)
            if re.match(regex, option):
                return option
            print("The response is invalid")

    def exit(self) -> None:
        confirm: str = self.ask_option_no_case("Are you sure?", ["yes", "no"])
        if confirm == "yes":
            self.running = False
