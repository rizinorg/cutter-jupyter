import cutter

from PySide2.QtWidgets import QAction

from .manager import JupyterManager
from .widget import JupyterWidget


class JupyterPlugin(cutter.CutterPlugin):
    def setupPlugin(self):
        self._jupyter_manager = JupyterManager()
        self._jupyter_manager.start()

    def setupInterface(self, main):
        action = QAction("Jupyter", main)
        action.setCheckable(True)
        widget = JupyterWidget(self._jupyter_manager, main, action)
        main.addPluginDockWidget(widget, action)

    def terminate(self):
        self._jupyter_manager.stop()
