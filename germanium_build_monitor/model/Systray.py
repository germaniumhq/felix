from mopyx import model, action

from .SystrayItem import SystrayItem

from germanium_build_monitor.model import Settings


@model
class Systray:
    def __init__(self):
        self.requests = []
        self.items = []

    @action
    def add_request(self, item: SystrayItem):
        self.requests.insert(0, item)

    @action
    def flush_requests(self):
        unique_requests = []

        for request in self.requests:
            if request not in unique_requests:
                unique_requests.append(request)

        for request in unique_requests:
            self.items.insert(0, request)

        if len(self.items) > Settings.settings.systray_items_count:
            del self.items[Settings.settings.systray_items_count:]

