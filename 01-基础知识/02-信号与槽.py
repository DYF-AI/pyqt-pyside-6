import sys
from PySide6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
from PySide6.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        mainlayout = QVBoxLayout()

        button = QPushButton("按钮")
        button.clicked.connect(self.hello)

        mainlayout.addWidget(button)
        self.setLayout(mainlayout)

    def hello(self):
        print("hello world!")

if __name__ == "__main__":
    # app = QApplication(sys.argv)
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()