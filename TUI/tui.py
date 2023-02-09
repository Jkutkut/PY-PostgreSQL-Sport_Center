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
#    Updated: 2023/02/09 12:52:24 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import re

class TUI:
    def __init__(self, options) -> None:
        self.running = True
        self.options = options
        self.options.append(TUI.newOption("exit", self.exit))

    def newOption(name: str, ft) -> dict:
        return {"name": name, "ft": ft}

    def run(self) -> None:
        if not self.running:
            raise Exception("Execution ended")
        while self.running:
            r = self.askOptions(self.options)
            self.options[r]["ft"]()

    def ask(self, question: str, minlen = -1, maxlen = -1) -> str:
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

    def askOptions(self, options) -> int:
        opts = [f"{i + 1}: {options[i]['name']}" for i in range(len(options))]
        opts = "\nWhat do you want to do?\n" + "\n".join(opts) + "\n-> "
        while True:
            try:
                inp = self.ask(opts)
                if len(inp) == 0:
                    continue
                idx = int(inp) - 1
                if idx < 0 or idx >= len(options):
                    print(f"Invalid number: It should be in the range [1, {len(options)}].")
                else:
                    return idx
            except ValueError:
                print("Invalid number")

    def askOptionNoCase(self, question: str, options: list) -> str:
        question = question + " [" + "|".join(options) + "]\n-> "
        options = [o.lower() for o in options]
        while True:
            option = self.ask(question).lower()
            if not option in options:
                print("Please, select one of the options")
            else:
                return option
    def askRegex(self, question: str, regex: str) -> str:
        while True:
            option = self.ask(question)
            if re.match(regex, option):
                return option
            print("The response is invalid")

    def exit(self) -> None:
        #confirm = self.askOptionNoCase("Are you sure?", ["yes", "no"])
        #if confirm == "yes":
        #    self.running = False
        self.running = False # TODO
