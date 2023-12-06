import sys
from PySide6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
from login import Ui_Form


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.loginFuc)

    def loginFuc(self):
        # 账号
        account = self.lineEdit.text()
        # 密码
        password = self.lineEdit_2.text()

        if account == "123" and password == "123":
            print("登陆成功")
        else:
            print("登陆失败")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()