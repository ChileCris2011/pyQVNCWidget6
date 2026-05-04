#! /usr/bin/env python3

## This is just an internal testing file. Ignore it ;)

import sys
import logging

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QKeyEvent, QShortcut, QKeySequence
from PyQt6.QtCore import QSize
#from qvncwidget6 import QVNCWidget
from qvncwidget6.qvncwidget6 import QVNCWidget, QVNCWidgetGL

logging.basicConfig(
    filename="latest.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Window(QMainWindow):
    def __init__(self, app: QApplication):
        super(Window, self).__init__()

        self.app = app
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QVNCWidget")

        #self.vnc = QVNCWidgetGL(
        self.vnc = QVNCWidget(
            parent=self,
            host="127.0.0.1", port=5900,
            readOnly=False,
            autoResize=True
        )
        self.setCentralWidget(self.vnc)
        self.vnc.setFocus()
        self.vnc.setMouseTracking(False)
        self.vnc.onResize.connect(self.resize)
        self.vnc.start()
        self.shortcut = QShortcut(QKeySequence("Ctrl+L"), self)
        self.shortcut.activated.connect(self.toggle_restriction)
    
    def toggle_restriction(self):
        self.vnc.restricting = not self.vnc.restricting
        print("Restriction:", self.vnc.restricting)
    
    def mousePressEvent(self, a0):
        self.vnc.mousePressEvent(a0)
    
    def mouseReleaseEvent(self, a0):
        self.vnc.mouseReleaseEvent(a0)

    def keyPressEvent(self, ev: QKeyEvent):
        #print(ev.nativeScanCode(), ev.text(), ord(ev.text()), ev.key())
        self.vnc.keyPressEvent(ev)

    def keyReleaseEvent(self, ev: QKeyEvent):
        #print(ev.nativeScanCode(), ev.text(), ord(ev.text()), ev.key())
        self.vnc.keyReleaseEvent(ev)

    def closeEvent(self, ev):
        self.vnc.stop()
        return super().closeEvent(ev)

    def center(self):
        qr = self.frameGeometry()
        cp = self.app.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

logging.basicConfig(
    format="[%(name)s] %(levelname)s: %(message)s", level=logging.DEBUG
)

app = QApplication(sys.argv)
window = Window(app)
#window.setFixedSize(800, 600)
window.resize(800, 600)
window.center()
window.show()

sys.exit(app.exec())
