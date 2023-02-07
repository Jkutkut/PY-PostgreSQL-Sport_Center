from tui import TUI

class SportCenterTUI(TUI):
    def __init__(self):
        TUI.__init__(self, [{"name": "opt1", "ft": self.op1}])

    def op1(self):
        print("op1 selected")
