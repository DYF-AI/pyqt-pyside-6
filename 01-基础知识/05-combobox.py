
from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout
from login import Ui_Form


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        cb = QComboBox()
        cb.addItems(["李景文", "董永飞", "李景文"])

        # cb.currentIndexChanged.connect(lambda : print(cb.currentText()))
        # cb.currentTextChanged.connect(lambda : print(cb.currentText()))
        cb.currentTextChanged.connect(self.showName)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(cb)
        self.setLayout(mainLayout)

    def showName(self, name):
        print(name)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()