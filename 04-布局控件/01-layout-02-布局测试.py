from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 登陆界面
        self.mainLayout = QVBoxLayout()

        # self.userLayout = QHBoxLayout()
        # self.userLayout.addWidget(QLabel("用户名"))
        # self.userLayout.addWidget(QLineEdit())
        #
        # self.passwordLayout = QHBoxLayout()
        # self.passwordLayout.addWidget(QLabel("密码"))
        # self.passwordLayout.addWidget(QLineEdit())
        #
        # self.mainLayout.addLayout(self.userLayout)
        # self.mainLayout.addLayout(self.passwordLayout)
        # self.mainLayout.addWidget(QPushButton("登陆"))

        # self.formLayout = QFormLayout()
        # self.formLayout.addRow("用户名", QLineEdit())
        # self.formLayout.addRow("密码", QLineEdit())
        # self.formLayout.addWidget(QPushButton("登陆"))
        # self.mainLayout.addLayout(self.formLayout)

        # 网格控件
        self.gridLayout = QGridLayout()
        # self.gridLayout.addWidget(QPushButton("1"), 0, 0)
        # self.gridLayout.addWidget(QPushButton("2"), 0, 1)
        # self.gridLayout.addWidget(QPushButton("3"), 0, 2)
        # self.gridLayout.addWidget(QPushButton("4"), 1, 0, 1, 4)
        self.gridLayout.addWidget(QLabel("用户名"), 0, 0)
        self.gridLayout.addWidget(QLineEdit(), 0, 1)
        self.gridLayout.addWidget(QLabel("密码"), 1, 0)
        self.gridLayout.addWidget(QLineEdit(), 1, 1)
        self.gridLayout.addWidget(QPushButton("登陆"), 2, 1, 1, 2)

        self.mainLayout.addLayout(self.gridLayout)

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
