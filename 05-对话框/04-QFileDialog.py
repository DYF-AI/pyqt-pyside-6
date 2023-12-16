
"""
    QFileDialog
        - getOpenFileName 打开一个文件
        - getOpenFileNames 打开多个文件
        - getExistingDirectory 打开一个文件夹
        - getSaveFileName 保存一个文件

"""

from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QFileDialog,QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton("选择文件")
        btn1.clicked.connect(lambda : print(QFileDialog.getOpenFileName(self, # 窗体类型
                                                                       "选择文件标题", # 对话框标题
                                                                       "../",    # 打开文件的路径
                                                                       #"All File (*);;py文件(*.py *.pyd)" # 过滤文件，"所有文件(*.py);;音频文件mp3(.mp3 *.mp4 *.music)"
                                                                       "所有文件(*.py);;音频文件mp3(.mp3 *.mp4 *.music)"
                                                                       )))
        btn2 = QPushButton("选择多个文件")
        btn2.clicked.connect(lambda: print(QFileDialog.getOpenFileNames(self,  # 窗体类型
                                                                       "选择多个文件标题",  # 对话框标题
                                                                       "../",  # 打开文件的路径
                                                                       # "All File (*);;py文件(*.py *.pyd)" # 过滤文件，"所有文件(*.py);;音频文件mp3(.mp3 *.mp4 *.music)"
                                                                       "所有文件(*.py);;音频文件mp3(.mp3 *.mp4 *.music)"
                                                                       )))

        btn3 = QPushButton("打开文件夹")
        btn3.clicked.connect(lambda: print(QFileDialog.getExistingDirectory(self,
                                                                            "选择文件夹标题",
                                                                            "../")))

        btn4 = QPushButton("保存文件")
        btn4.clicked.connect(lambda: print(QFileDialog.getSaveFileName(self,
                                                                      "选择保存文件标题",
                                                                       ".",
                                                                       "所有文件(*.py);;音频文件mp3(.mp3 *.mp4 *.music)"
                                                                       )))


        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(btn1)
        self.mainLayout.addWidget(btn2)
        self.mainLayout.addWidget(btn3)
        self.mainLayout.addWidget(btn4)
        self.setLayout(self.mainLayout)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()