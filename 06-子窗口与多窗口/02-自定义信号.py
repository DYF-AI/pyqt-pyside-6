from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Signal

"""
    主要解决主窗口和子窗口之间的通信问题
    - 主窗口向子窗口传参
"""


class MyWindow(QWidget):
    # sendValueToSubWindow = Signal(object)
    sendValueToSubWindow = Signal(str)

    def __init__(self):
        super().__init__()

        self.lineEditSend = QLineEdit()
        self.btn = QPushButton("发送数据到子窗口")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEditSend)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        self.subWindow = SubWindow()
        self.sendValueToSubWindow.connect(self.subWindow.lineEditSub.setText)
        self.btn.clicked.connect(self.sendValue)
        self.subWindow.show()

    def sendValue(self):
        text = self.lineEditSend.text()
        self.sendValueToSubWindow.emit(text)


class SubWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 接受
        self.lineEditSub = QLineEdit()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEditSub)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
