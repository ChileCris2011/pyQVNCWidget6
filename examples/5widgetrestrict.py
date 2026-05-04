"""
Example for QVNCWidget restricting the cursor to the widget (v1.0.8)
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QShortcut, QKeySequence
from qvncwidget6 import QVNCWidget

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QVNCWidget")

        self.vnc = QVNCWidget(
            parent=self,
            host="127.0.0.1", port=5900,
            password="1234",
            readOnly=False
        )

        self.setCentralWidget(self.vnc)

        # we need to request focus otherwise we will not get keyboard input events
        self.vnc.setFocus()

        # we need to disable this, as we send the movement data directly
        self.vnc.setMouseTracking(False)

        self.vnc.start()

        # shortcut to lock/unlock the mouse
        self.shortcut = QShortcut(QKeySequence("Ctrl+L"), self)
        self.shortcut.activated.connect(self.toggle_restriction)

    def toggle_restriction(self):
        self.vnc.restricting = not self.vnc.restricting
        print("Restricition:", self.vnc.restricting)

    def closeEvent(self, ev):
        self.vnc.stop()
        return super().closeEvent(ev)

app = QApplication(sys.argv)
window = Window()
window.resize(800, 600)
window.show()

sys.exit(app.exec())