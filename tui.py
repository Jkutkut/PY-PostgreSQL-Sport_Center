class TUI:
    def __init__(self, options) -> None:
        self.running = True
        self.options = options
        self.options.append({"name": "exit", "ft": self.exit})

    def run(self) -> None:
        while self.running:
            r = self.askOptions(self.options)
            self.options[r]["ft"]()

    def ask(self, question: str) -> str:
        r = input(question).strip()
        print()
        return r

    def askOptions(self, options) -> int:
        opts = [f"{i + 1}: {options[i]['name']}" for i in range(len(options))]
        opts = "\n".join(opts) + "\n-> "
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
        question = question + " [" + "|".join(options) + "]"
        options = [o.lower() for o in options]
        while True:
            option = self.ask(question).lower()
            if not option in options:
                print("Please, select one of the options")
            else:
                return option

    def exit(self) -> None:
        confirm = self.askOptionNoCase("Are you sure?", ["yes", "no"])
        if confirm == "yes":
            self.running = False
