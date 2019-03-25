
import cutter

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QPushButton

from .autogen import icons_rc # not unused! need to register the resources.


class JupyterWidget(cutter.CutterDockWidget):
    def __init__(self, jupyter_manager, parent, action):
        super(JupyterWidget, self).__init__(parent, action)
        self._jupyter_manager = jupyter_manager
        self.setObjectName("JupyterWidget")
        self.setWindowTitle("Jupyter")

        self._tab_widget = QTabWidget(self)
        self.setWidget(self._tab_widget)

        corner_widget = QWidget(self._tab_widget)
        corner_widget_layout = QHBoxLayout(corner_widget)
        corner_widget.setLayout(corner_widget_layout)
        corner_widget_layout.setContentsMargins(4, 4, 4, 4)
        self._home_button = QPushButton(corner_widget)
        self._home_button.setStyleSheet("""
            QPushButton { padding: 2px; background-color: palette(light); border-radius: 4px; 
            QPushButton:pressed { background-color: palette(dark); }""")
        self._home_button.setIcon(QIcon(":cutter_jupyter/home.svg"))
        self._home_button.setEnabled(False)
        corner_widget_layout.addWidget(self._home_button)
        self._tab_widget.setCornerWidget(corner_widget)

        self._setup_ui_without_webengine()

    def _setup_ui_without_webengine(self):
        self._clear_tabs()

        page = QWidget(self)
        layout = QVBoxLayout(page)
        page.setLayout(layout)

        label = QLabel(page)
        label.setTextFormat(Qt.RichText)
        label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        label.setOpenExternalLinks(True)
        label.setText("""
            QtWebEngine is not available.<br />
            Open the following URL in your Browser to use Jupyter:<br />
            <a href="{0}">{0}</a>""".format(self._jupyter_manager.app.url_with_token))
        layout.addWidget(label)
        layout.setAlignment(label, Qt.AlignCenter)

        self._tab_widget.addTab(page, "Jupyter")
        self._tab_widget.setTabsClosable(False)

    def _setup_ui_with_webengine(self):
        self._clear_tabs()
        pass

    def _clear_tabs(self):
        while self._tab_widget.count() > 0:
            pass

    def _remove_tab(self, index):
        widget = self._tab_widget.widget(index)
        self._tab_widget.removeTab(widget)
        widget.setParent(None)
