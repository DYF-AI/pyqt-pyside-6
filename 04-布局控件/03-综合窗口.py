
from PySide6.QtWidgets import (QApplication,
                               QWidget,
                               QVBoxLayout,
                               QPushButton,
                               QLabel,
                               QLineEdit,
                               QComboBox,
                               QCheckBox,
                               QButtonGroup,
                               QRadioButton,
                               QTextEdit,
                               QPlainTextEdit,
                               QSlider)
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.mainLayout = QVBoxLayout()
        self.label1 = QLabel("标签1")
        self.label1.setText("标签1被修改了")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter) # 居中
        self.btn1 = QPushButton("按钮1")

        # 输入框
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("请输入内容")
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password) # 密码模式

        # 下拉框
        self.combobox = QComboBox()
        self.combobox.setPlaceholderText("请选择")
        self.combobox.addItems(["选项1", "选项2", "选项3"])
        self.combobox.removeItem(0)

        # 复选框
        self.checkBox1 = QCheckBox("复选框1")
        # self.checkBox1.setCheckable(False)
        self.checkBox1.setChecked(True)
        self.checkBox2 = QCheckBox("复选框2")

        # 创建单选按钮
        self.genderMan = QRadioButton("男")
        self.genderWoMan = QRadioButton("女")

        # 创建单选按钮组
        self.favoriteGroup = QButtonGroup()
        self.radiobtnMath = QRadioButton("数学")
        self.radiobtnChinese = QRadioButton("语文")
        self.favoriteGroup.addButton(self.radiobtnMath)
        self.favoriteGroup.addButton(self.radiobtnChinese)


        markdownStr = """
# 标题1
```python
def hello():
    return 'hello'
```

- 1
- 2
- 3

---

这是一段正常文字
        """
        # 创建文本框
        self.richText = QTextEdit()
        self.richText.setPlaceholderText("请输入内容")
        #self.richText.setMarkdown(markdownStr)
        #self.richText.setHtml('<h1>标题1</h1><p>这是一段正常的文字</p>')
        self.richText.setPlainText("这是一段正常的文字")

        self.plainText = QPlainTextEdit()
        self.plainText.setPlainText("这是一个纯文本框")

        # 滑条
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setRange(10,100)

        self.mainLayout.addWidget(self.label1)
        self.mainLayout.addWidget(self.btn1)
        self.mainLayout.addWidget(self.lineEdit)
        self.mainLayout.addWidget(self.combobox)
        self.mainLayout.addWidget(self.checkBox1)
        self.mainLayout.addWidget(self.checkBox2)
        self.mainLayout.addWidget(self.genderMan)
        self.mainLayout.addWidget(self.genderWoMan)
        self.mainLayout.addWidget(self.radiobtnMath)
        self.mainLayout.addWidget(self.radiobtnChinese)
        self.mainLayout.addWidget(self.richText)
        self.mainLayout.addWidget(self.plainText)
        self.mainLayout.addWidget(self.slider)

        self.setLayout(self.mainLayout)

        self.bind()
    def bind(self):
        self.btn1.clicked.connect(self.btn1_clicked)
        self.lineEdit.textChanged.connect(self.lineEdit_textChange)
        self.lineEdit.returnPressed.connect(self.lineEdit_returnPressed) # 回车键
        self.combobox.currentTextChanged.connect(self.comboboxTextChange)
        self.checkBox1.stateChanged.connect(self.checkBox1Change)
        self.checkBox2.stateChanged.connect(self.checkBox2Change)
        # 单选按钮的信号与槽的绑定
        self.genderMan.clicked.connect(lambda : print("男"))
        self.genderWoMan.clicked.connect(lambda : print("女"))
        self.favoriteGroup.buttonClicked.connect(self.whichButtonClick)

        self.richText.textChanged.connect(lambda : print("文本框内容发生了变化"))

        self.slider.valueChanged.connect(lambda x: print(f"滑条的值发生了变化:{x}"))


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

    def whichButtonClick(self):
        print("单选按钮组被点击了")
        print(f"选中的是:{self.favoriteGroup.checkedButton().text()}")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()