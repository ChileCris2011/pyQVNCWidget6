"""
Example for QVNCWidget6 usin onResize signal (v0.1.0)
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QSize
from qvncwidget6 import QVNCWidget

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QVNCWidget")

        self.vnc = QVNCWidget(
            parent=self,
            host="127.0.0.1", port=5900,
            password="1234",
            readOnly=True,
            autoResize=True
        )

        self.setCentralWidget(self.vnc)

        self.vnc.onResize.connect(self.resize)

        self.vnc.start()

    def closeEvent(self, ev):
        self.vnc.stop()
        return super().closeEvent(ev)

app = QApplication(sys.argv)
window = Window()
window.resize(800, 600)
window.show()

sys.exit(app.exec())