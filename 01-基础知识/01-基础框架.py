import sys
from PySide6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
from PySide6.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # btn = QPushButton("按钮", self)
        # btn.setGeometry(0, 0, 200, 100)
        # btn.setToolTip("点我有惊喜哟")
        # btn.setText("我被重新设置了")

        # mainLayout = QVBoxLayout()
        # lb = QLabel("我是一个标签", self)
        # lb.setText("我是被修改的文字")

        mainlayout = QVBoxLayout()
        line = QLineEdit(self)
        line.setPlaceholderText("请输入内容")
        mainlayout.addWidget(line)
        self.setLayout(mainlayout)

if __name__ == "__main__":
    # app = QApplication(sys.argv)
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()