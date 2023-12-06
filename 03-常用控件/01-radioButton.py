from PySide6.QtWidgets import QWidget, QApplication, QLabel, QRadioButton, QHBoxLayout,  QVBoxLayout, QButtonGroup

"""
    直接使用代码进行编写
"""
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 分组1
        self.group1 = QButtonGroup(self)
        label1 = QLabel("请选择你的编程语言")
        btn1 = QRadioButton("Python")
        btn2 = QRadioButton("JavaScript")
        btn3 = QRadioButton("C++")
        btn4 = QRadioButton("Java")
        self.group1.addButton(btn1)
        self.group1.addButton(btn2)
        self.group1.addButton(btn3)
        self.group1.addButton(btn4)

        btn1.clicked.connect(self.change_text)
        btn2.clicked.connect(self.change_text)
        btn3.clicked.connect(self.change_text)
        btn4.clicked.connect(self.change_text)

        # 分组2
        self.group2 = QButtonGroup(self)
        label2 = QLabel("请输入你的平均敲代码时间")
        btn5 = QRadioButton("1h")
        btn6 = QRadioButton("2h")
        btn7 = QRadioButton("3h")
        btn8 = QRadioButton("4h")
        self.group2.addButton(btn5)
        self.group2.addButton(btn6)
        self.group2.addButton(btn7)
        self.group2.addButton(btn8)

        btn5.clicked.connect(self.change_text)
        btn6.clicked.connect(self.change_text)
        btn7.clicked.connect(self.change_text)
        btn8.clicked.connect(self.change_text)

        # 显示标签
        self.label_show = QLabel("请选择编程语言和时间:")

        # 调整布局
        h1 = QHBoxLayout()
        h1.addWidget(label1)
        h1.addWidget(btn1)
        h1.addWidget(btn2)
        h1.addWidget(btn3)
        h1.addWidget(btn4)

        h2 = QHBoxLayout()
        h2.addWidget(label2)
        h2.addWidget(btn5)
        h2.addWidget(btn6)
        h2.addWidget(btn7)
        h2.addWidget(btn8)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(h1)
        mainLayout.addLayout(h2)
        mainLayout.addWidget(self.label_show)

        self.setLayout(mainLayout)

    def change_text(self):
        language = self.group1.checkedButton()
        time = self.group2.checkedButton()
        if language is not None and time is not None:
            self.label_show.setText(
                f"你的编程语言是：{language.text()}, 你平均敲代码时间是： {time.text()}"
            )

if __name__ == "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()