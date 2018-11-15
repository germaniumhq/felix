from typing import Dict, Any
from mopyx import model


@model
class Settings:
    def __init__(self,
                 systray_items_count: int = 2,
                 main_grid_columns: int = 3,
                 last_builds_count: int = 5,
                 notification_display_time: int = 8,
                 ) -> None:
        self.systray_items_count: int = systray_items_count
        self.main_grid_columns: int = main_grid_columns
        self.last_builds_count: int = last_builds_count
        self.notification_display_time: int = notification_display_time

    def as_dict(self) -> Dict[str, Any]:
        return {
            "systray_items_count": self.systray_items_count,
            "main_grid_columns": self.main_grid_columns,
            "last_builds_count": self.last_builds_count,
            "notification_display_time": self.notification_display_time,
        }

    @staticmethod
    def from_dict(d) -> 'Settings':
        return Settings(
            systray_items_count=d['systray_items_count'],
            main_grid_columns=d['main_grid_columns'],
            last_builds_count=d['last_builds_count'],
            notification_display_time=d['notification_display_time'],
        )


settings: Settings = Settings()

