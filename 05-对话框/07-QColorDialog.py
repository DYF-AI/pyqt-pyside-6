from PySide6.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.edit = QTextEdit()
        self.btn1 = QPushButton("点我选择字体")
        self.btn1.clicked.connect(self.changeFont)

        self.btn2 = QPushButton("点我修改颜色")
        self.btn2.clicked.connect(self.changeFontColor)


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.edit)
        self.mainLayout.addWidget(self.btn1)
        self.mainLayout.addWidget(self.btn2)
        self.setLayout(self.mainLayout)

    def changeFont(self):
        ok, font = QFontDialog.getFont()
        if not ok : return
        self.edit.setFont(font)

    def changeFontColor(self):
        color = QColorDialog.getColor()
        self.edit.setTextColor(color)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()