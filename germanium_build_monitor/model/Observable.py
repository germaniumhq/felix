from typing import Dict, Callable, Any

import uuid


class RegistrationHandler:
    def __init__(self, observable: 'Observable', event_name: str, callback_id: str):
        """ Create a registration handler. """
        self.observable = observable
        self.event_name = event_name
        self.callback_id = callback_id

    def detach(self) -> None:
        del (self.observable._listeners[self.event_name])[self.callback_id]


class Observable():
    def __init__(self) -> None:
        self._listeners: Dict[str, Dict[str, Callable[[Any], Any]]] = dict()

    def on_event(self,
                 event_name: str,
                 callback: Callable[[Any], Any]) -> RegistrationHandler:

        listener_map = self._listeners.get(event_name, None)

        if not listener_map:
            listener_map = dict()
            self._listeners[event_name] = listener_map

        callback_id = str(uuid.uuid4())
        listener_map[callback_id] = callback

        return RegistrationHandler(self, event_name, callback_id)

    def notify_observers(self,
                         event_name: str,
                         data: Any) -> None:
        listener_map = self._listeners.get(event_name, None)

        if not listener_map:
            return

        for k, callback in listener_map.items():
            callback(data)
