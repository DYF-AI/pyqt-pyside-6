
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPlainTextEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # textEdit = QTextEdit()
        #textEdit.setHtml("<h1>这是一个标题</h1><b>这是一个粗体</b><i>这是一个斜体</i>")
        #textEdit.setMarkdown("# 这是一个大标题 ")

        textEdit = QPlainTextEdit()
        textEdit.setPlainText("这是一个大标题 ")
        textEdit.appendPlainText("这是一个大标题 ")
        btn = QPushButton("追加文本")
        btn.clicked.connect(lambda : textEdit.appendPlainText("这是一个段落"))

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(textEdit)
        self.mainLayout.addWidget(btn)

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()