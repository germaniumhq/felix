from mopyx import model


@model
class Settings:
    def __init__(self):
        self.systray_items_count: int = 2
        self.main_grid_columns: int = 3


settings: Settings = Settings()

