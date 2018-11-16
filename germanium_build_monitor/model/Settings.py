from typing import Dict, Any
from mopyx import model


@model
class Settings:
    def __init__(self,
                 systray_items_count: int = 2,
                 main_page_items: int = 100,
                 last_builds_count: int = 5,
                 notification_display_time: int = 8,
                 ) -> None:
        self.systray_items_count: int = systray_items_count
        self.main_page_items: int = main_page_items
        self.last_builds_count: int = last_builds_count
        self.notification_display_time: int = notification_display_time

    def as_dict(self) -> Dict[str, Any]:
        return {
            "systray_items_count": self.systray_items_count,
            "main_page_items": self.main_page_items,
            "last_builds_count": self.last_builds_count,
            "notification_display_time": self.notification_display_time,
        }

    @staticmethod
    def from_dict(d) -> 'Settings':
        return Settings(
            systray_items_count=d['systray_items_count'],
            main_page_items=d.get('main_page_items', 100),
            last_builds_count=d['last_builds_count'],
            notification_display_time=d['notification_display_time'],
        )


settings: Settings = Settings()

