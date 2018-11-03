from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QMovie

from germanium_build_monitor.ui.Ui_LoadingFrame import Ui_Form
from germanium_build_monitor.resources import icons


class LoadingFrame(QWidget, Ui_Form):
    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)

        self.setupUi(self)

        movie = QMovie(icons.get_icon_path("loader.gif"))
        self.load_image_label.setMovie(movie)

        movie.start()

