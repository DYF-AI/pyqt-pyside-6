from PySide6.QtWidgets import QApplication, QWidget,QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QTimer
import os

os.chdir(os.path.dirname(__file__))

class LodingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("加载窗口")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.mousePressed = False # 表示鼠标是否被按下
        self.offsetX = 0 # 鼠标相对于窗口的x轴偏移量
        self.offsetY = 0 # 鼠标相对于窗口的y轴偏移量

        self.pixmap = QPixmap("../05-对话框/20231216204952.jpg")
        self.size = self.pixmap.size()
        self.pic = QLabel(self)
        self.pic.setFixedSize(300, 200)
        self.pic.setPixmap(self.pixmap)
        self.pic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pic.setScaledContents(True)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.pic)
        self.setLayout(self.mainLayout)
        QTimer.singleShot(3000, self.openMainWindow)

    def openMainWindow(self):
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePressed = True
            self.offsetX = event.globalPosition().x() - self.pos().x()
            self.offsetY = event.globalPosition().y() - self.pos().y()

    def mouseMoveEvent(self, event) -> None:
        if self.mousePressed:
            x = event.globalPosition().x() - self.offsetX
            y = event.globalPosition().y() - self.offsetY

    def mouseReleaseEvent(self, event) -> None:
        if event.button() == Qt.LeftButton:
            self.mousePressed = False

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        self.lbWelcome = QLabel("欢迎使用本软件")
        self.lbWelcome.setFont(QFont("微软雅黑", 50))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lbWelcome)
        self.setLayout(self.mainLayout)

if __name__ == "__main__":
    app = QApplication([])
    window = LodingWindow()
    window.show()
    app.exec()
