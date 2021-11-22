import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class GitYellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.repaint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        r1 = randint(10, 50)
        r2 = randint(10, 50)
        qp.drawEllipse(randint(50, 450), randint(50, 450), r1, r1)
        qp.drawEllipse(randint(50, 450), randint(50, 450), r2, r2)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    git_yellow_circles = GitYellowCircles()
    git_yellow_circles.show()
    sys.exit(app.exec())



