from PySide6.QtWidgets import QWidget,QApplication,QDialog,QVBoxLayout,QInputDialog, QPushButton, QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)

        self.btn1 = QPushButton("获取一个整型数字")
        self.btn1.clicked.connect(self.getIntDialog)
        # replay = QInputDialog.getInt(self, "标题", "内容", 1, 0, 100, 1)

        self.btn2 = QPushButton("获取一个浮点数字")
        self.btn2.clicked.connect(self.getFloatDialog)

        self.btn3 = QPushButton("获取一个Item")
        self.btn3.clicked.connect(lambda : print(QInputDialog.getItem(self, "标题", "内容", ["a", "b", "c"], 0, False)))

        self.btn4 = QPushButton("获取单行文字")
        self.btn4.clicked.connect(lambda: print(QInputDialog.getText(self, "标题", "内容",
                                                                     # QLineEdit.EchoMode.NoEcho,
                                                                     QLineEdit.EchoMode.Normal,
                                                                     "默认值")))

        self.btn5 = QPushButton("获取多行文字")
        self.btn5.clicked.connect(lambda: print(QInputDialog.getMultiLineText(self, "标题", "内容")))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btn1)
        self.mainLayout.addWidget(self.btn2)
        self.mainLayout.addWidget(self.btn3)
        self.mainLayout.addWidget(self.btn4)
        self.mainLayout.addWidget(self.btn5)
        self.setLayout(self.mainLayout)

    def getIntDialog(self):
        replay, ok = QInputDialog.getInt(self,
                                         "标题",
                                         "内容",
                                         1,  # 默认值
                                         0,  # 最小值
                                         100,# 最大值
                                         1)  # 步长

        if ok:
            print(replay)

    def getFloatDialog(self):
        replay, ok = QInputDialog.getDouble(self,
                                         "标题",
                                         "内容",
                                         1.0,  # 默认值
                                         0.0,  # 最小值
                                         100.0,# 最大值
                                         1)  # 步长

        if ok:
            print(replay)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()