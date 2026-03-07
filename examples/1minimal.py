"""
Minimal example for QVNCWidget6 (v0.1.0)
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from qvncwidget6 import QVNCWidget

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QVNCWidget")

        self.vnc = QVNCWidget(
            parent=self,
            host="127.0.0.1", port=5900,
            password="1234",
            readOnly=True
        )

        self.setCentralWidget(self.vnc)

        # if you want to resize the window to the resolution of the 
        # VNC remote device screen, you can do this
        self.vnc.onInitialResize.connect(self.resize)

        self.vnc.start()

    def closeEvent(self, ev):
        self.vnc.stop()
        return super().closeEvent(ev)

app = QApplication(sys.argv)
window = Window()
window.resize(800, 600)
window.show()

sys.exit(app.exec())