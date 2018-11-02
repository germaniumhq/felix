from mopyx import model


@model
class SystrayItem:
    def __init__(self, systray: bool) -> None:
        self.systray = systray
