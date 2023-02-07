from tui import TUI

class SportCenterTUI(TUI):
    def __init__(self):
        TUI.__init__(
            self,
            [
                TUI.newOption("op1", self.op1),
                TUI.newOption("op2", self.op1)
            ]
        )

    def op1(self):
        print("op1 selected")
