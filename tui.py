class TUI:
    def __init__(self, options) -> None:
        self.running = True
        self.options = options
        self.options.append({"name": "exit", "ft": self.exit})

    def run(self) -> None:
        while self.running:
            r = self.askOptions(self.options)
            self.options[r]["ft"]()

    def askOptions(self, options) -> None:
        opts = [f"{i + 1}: {options[i]['name']}" for i in range(len(options))]
        opts = "\n".join(opts) + "\n-> "
        while True:
            try:
                idx = int(input(opts)) - 1
                print("\n")
                if idx < 0 or idx >= len(options):
                    print(f"Invalid number: It should be in the range [1, {len(options)}].")
                else:
                    return idx
            except ValueError:
                print("\nInvalid number")


    def exit(self) -> None:
        # TODO
        self.running = False
