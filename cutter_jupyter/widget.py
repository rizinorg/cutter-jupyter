
import cutter

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget, QTabWidget, QPushButton

try:
    from PySide2.QtWebEngine import QtWebEngine
    from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
    webengine_available = False
except ImportError:
    webengine_available = False

if webengine_available:
    QtWebEngine.initialize()


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
            QPushButton { padding: 2px; background-color: palette(light); border-radius: 4px; }
            QPushButton:pressed { background-color: palette(dark); }""")
        self._home_button.setIcon(QIcon(":cutter_jupyter/home.svg"))
        self._home_button.setEnabled(False)
        corner_widget_layout.addWidget(self._home_button)
        self._tab_widget.setCornerWidget(corner_widget)

        if webengine_available:
            self._setup_ui_with_webengine()
        else:
            self._setup_ui_without_webengine()

        self._home_button.clicked.connect(self._open_home_tab)
        self._tab_widget.tabCloseRequested.connect(self._tab_close_requested)


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
        self._tab_widget.setTabsClosable(True) # TODO: False

    def _setup_ui_with_webengine(self):
        self._clear_tabs()
        self._open_home_tab()
        self._tab_widget.setTabsClosable(True)
        self._home_button.setEnabled(True)

    def _tab_close_requested(self, index):
        self._remove_tab(index)
        if self._tab_widget.count() == 0:
            self._open_home_tab()

    def _open_home_tab(self):
        if not webengine_available:
            return
        url = self._jupyter_manager.app.url_with_token
        if url is None:
            return
        tab = self.create_new_tab()
        tab.load(url)

    def create_new_tab(self):
        web_view = JupyterWebView(self, self._tab_widget)
        index = self._tab_widget.addTab(web_view, "Tab")
        web_view.set_tab_widget(self._tab_widget)
        self._tab_widget.setCurrentIndex(index)
        return web_view

    def _clear_tabs(self):
        while self._tab_widget.count() > 0:
            pass

    def _remove_tab(self, index):
        widget = self._tab_widget.widget(index)
        self._tab_widget.removeTab(widget)
        #widget.setParent(None)


class JupyterWebView(QWebEngineView):
    def __init__(self, jupyter_widget, parent):
        super(JupyterWebView, self).__init__(parent)
        self._jupyter_widget = jupyter_widget
        self._tab_widget = None

        self.titleChanged.connect(self._update_title)
        self._update_title()

    def set_tab_widget(self, tab_widget):
        self._tab_widget = tab_widget
        self._update_title()

    def _update_title(self):
        if self._tab_widget is None:
            return
        title = self.title()
        if title is None:
            title = "Jupyter"
        self._tab_widget.setTabText(self._tab_widget.indexOf(self), title)

    def createWindow(self, type, *args, **kwargs):
        if type == QWebEnginePage.WebBrowserTab:
            return self._jupyter_widget.create_new_tab()
