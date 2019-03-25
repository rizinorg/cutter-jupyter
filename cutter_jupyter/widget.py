import cutter


class JupyterWidget(cutter.CutterDockWidget):
    def __init__(self, parent, action):
        super(JupyterWidget, self).__init__(parent, action)

        self.setWindowTitle("Jupyter")

    def set_url(self, url):
        pass
