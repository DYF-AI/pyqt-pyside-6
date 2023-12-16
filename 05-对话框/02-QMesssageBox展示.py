from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.btn = QPushButton("按钮")
        self.btn.clicked.connect(self.btnClicked)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btn)
        self.setLayout(self.mainLayout)

    def btnClicked(self):
        # 图标的变化
        # QMessageBox.information(self, "你好", "你好，世界！")
        # QMessageBox.question(self, "你好", "你好，世界！")
        # QMessageBox.warning(self, "你好", "你好，世界！")
        # QMessageBox.critical(self, "你好", "你好，世界！")
        # QMessageBox.about(self, "你好", "你好，世界！")

        replay = QMessageBox.information(self, "标题", "内容",
                                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Apply, # 按键列表
                                QMessageBox.StandardButton.Ok) # 默认按键

        s = "你点击了"
        if replay == QMessageBox.StandardButton.Ok:
            print(f"{s}OK")
        elif replay == QMessageBox.StandardButton.No:
            print(f"{s}No")
        elif replay == QMessageBox.StandardButton.Discard:
            print(f"{s}Discard")
        elif replay == QMessageBox.StandardButton.Apply:
            print(f"{s}Apply")

if __name__ == "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()
