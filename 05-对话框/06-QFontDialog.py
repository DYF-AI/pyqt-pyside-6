from PySide6.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.edit = QTextEdit()
        self.btn = QPushButton("点我选择字体")
        self.btn.clicked.connect(self.changeFont)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.edit)
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

    def changeFont(self):
        ok, font = QFontDialog.getFont()
        if not ok : return
        self.edit.setFont(font)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()