from PySide2.QtWidgets import QDialog, QWidget


class WidgetSwitcher:
    def __init__(self,
                 widget_holder: QWidget):
        self.widget_holder = widget_holder
        self._last_widget = None

    def set(self, widget: QWidget):
        if self._last_widget:
            self._last_widget.deleteLater()
            self.widget_holder.removeWidget(self._last_widget)

        self.widget_holder.addWidget(widget)
        self._last_widget = widget
