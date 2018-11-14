from mopyx import model


@model
class Settings:
    def __init__(self,
                 systray_items_count: int = 2,
                 main_grid_columns: int = 3,
                 last_builds_count: int = 5,
        ):
        self.systray_items_count: int = systray_items_count
        self.main_grid_columns: int = main_grid_columns
        self.last_builds_count: int = last_builds_count

    def as_dict(self):
        return {
            "systray_items_count": self.systray_items_count,
            "main_grid_columns": self.main_grid_columns,
            "last_builds_count": self.last_builds_count,
        }

    @staticmethod
    def from_dict(d) -> 'Settings':
        return Settings(
            systray_items_count=d['systray_items_count'],
            main_grid_columns=d['main_grid_columns'],
            last_builds_count=d['last_builds_count'],
        )


settings: Settings = Settings()

