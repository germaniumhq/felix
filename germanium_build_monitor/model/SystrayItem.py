from .Observable import Observable


class SystrayItem(Observable):
    def __init__(self, systray: bool) -> None:
        super().__init__()

        self.systray = systray

