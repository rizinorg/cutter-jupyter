import cutter

from . import manager

class JupyterPlugin(cutter.CutterPlugin):
    def setupPlugin(self):
        self._jupyter_manager = manager.JupyterManager()
        self.notebook_app = self._jupyter_manager.start_jupyter()
        print("STARTED: {}".format(self.notebook_app.url_with_token))

    def setupInterface(self, main):
        pass

    def terminate(self):
        pass
