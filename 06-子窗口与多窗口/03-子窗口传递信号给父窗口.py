from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Signal

"""
    子窗口传递信号给父窗口
"""


class MyWindow(QWidget):
    sendValueToSubWindow = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")

        self.lineEditShow = QLineEdit()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEditShow)
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        self.subWindow = SubWindow(self) # 把父窗口传进去
        self.subWindow.show()


class SubWindow(QWidget):
    sendValueToMain = Signal(str)

    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("子窗口")
        self.parent = parent
        self.move(400, 400)

        self.lineEditSub = QLineEdit()
        self.btn = QPushButton("发送数据到主窗口")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEditSub)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)
        self.bind()


    def bind(self):
        self.sendValueToMain.connect(self.parent.lineEditShow.setText)
        self.btn.clicked.connect(self.sendValue)

    def sendValue(self):
        self.sendValueToMain.emit(self.lineEditSub.text())


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
