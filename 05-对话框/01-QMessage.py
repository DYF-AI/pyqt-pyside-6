
from PySide6.QtWidgets import QApplication, QWidget,QVBoxLayout, QMessageBox, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("按钮")
        self.btn.clicked.connect(self.btnClicked)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

    def btnClicked(self):
        reply = QMessageBox.information(self, "你好", "你好，世界！", QMessageBox.StandardButton.Ok  |
                                        QMessageBox.StandardButton.No | QMessageBox.StandardButton.Discard,
                                        QMessageBox.StandardButton.Ok)

        print(reply)
        if reply == QMessageBox.StandardButton.Ok:
            print("你点了Ok")
        elif reply == QMessageBox.StandardButton.No:
            print("你点了No")
        elif reply == QMessageBox.StandardButton.Discard:
            print("你点了Discard")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()