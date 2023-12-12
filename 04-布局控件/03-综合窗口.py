
from PySide6.QtWidgets import QApplication, QWidget,\
    QVBoxLayout,QPushButton,QLabel,QLineEdit,QComboBox,QCheckBox
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.mainLayout = QVBoxLayout()
        self.label1 = QLabel("标签1")
        self.label1.setText("标签1被修改了")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter) # 居中
        self.btn1 = QPushButton("按钮1")
        self.btn1.clicked.connect(self.btn1_clicked)

        # 输入框
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("请输入内容")
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password) # 密码模式
        self.lineEdit.textChanged.connect(self.lineEdit_textChange)
        self.lineEdit.returnPressed.connect(self.lineEdit_returnPressed) # 回车键

        # 下拉框
        self.combobox = QComboBox()
        self.combobox.setPlaceholderText("请选择")
        self.combobox.addItems(["选项1", "选项2", "选项3"])
        self.combobox.removeItem(0)
        self.combobox.currentTextChanged.connect(self.comboboxTextChange)

        # 复选框
        self.checkBox1 = QCheckBox("复选框1")
        # self.checkBox1.setCheckable(False)
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(self.checkBox1Change)
        self.checkBox2 = QCheckBox("复选框2")
        self.checkBox2.stateChanged.connect(self.checkBox2Change)

        self.mainLayout.addWidget(self.label1)
        self.mainLayout.addWidget(self.btn1)
        self.mainLayout.addWidget(self.lineEdit)
        self.mainLayout.addWidget(self.combobox)
        self.mainLayout.addWidget(self.checkBox1)
        self.mainLayout.addWidget(self.checkBox2)
        self.setLayout(self.mainLayout)

    def btn1_clicked(self):
        print("按钮1被点击了")

    def lineEdit_textChange(self, text):
        print(f"文本框内容发生了变换: {text}")

    def lineEdit_returnPressed(self):
        print("文本框回车了")
        print(f"文本框的内容是:{self.lineEdit.text()}")

    def comboboxTextChange(self, text):
        print(f"下拉框内容发生了变化:{text}")

    def checkBox1Change(self, state):
        print(f"复选框1状态发生了变化:{state}")

    def checkBox2Change(self):
        print(f"复选框2状态为:{self.checkBox2.isChecked()}")


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()