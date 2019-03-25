
import cutter

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLabel, QVBoxLayout, QWidget


class JupyterWidget(cutter.CutterDockWidget):
    def __init__(self, jupyter_manager, parent, action):
        super(JupyterWidget, self).__init__(parent, action)
        self._jupyter_manager = jupyter_manager
        self.setObjectName("JupyterWidget")
        self.setWindowTitle("Jupyter")

        content = QWidget()
        self.setWidget(content)
        layout = QVBoxLayout(content)
        content.setLayout(layout)

        label = QLabel(content)
        label.setTextFormat(Qt.RichText)
        label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        label.setOpenExternalLinks(True)
        label.setText("""<a href="{0}">{0}</a>""".format(self._jupyter_manager.app.url_with_token))
        layout.addWidget(label)
