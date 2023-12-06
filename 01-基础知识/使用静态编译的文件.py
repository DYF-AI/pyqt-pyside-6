
from PySide6.QtWidgets import QApplication, QWidget
from login import Ui_Form
from ui_calculator import Ui_Form

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()