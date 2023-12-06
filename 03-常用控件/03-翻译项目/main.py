
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout

from ui_translate import Ui_Form
from youdao_api import connect


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fromLanguage = 0
        self.toLanguage = 0

        self.bind()

    def bind(self):
        self.pushButton.clicked.connect(self.translate)
        self.radioButton.clicked.connect(lambda : self.setFromLanguage(0))
        self.radioButton_2.clicked.connect(lambda : self.setFromLanguage(1))
        self.radioButton_3.clicked.connect(lambda : self.setFromLanguage(2))

        self.comboBox.currentIndexChanged.connect(lambda: self.setToLanguage(self.comboBox.currentIndex()+1))
        self.comboBox.setCurrentText("英语")

    def setFromLanguage(self, language):
        self.fromLanguage = language

    def setToLanguage(self, language):
        self.toLanguage = language

    def translate(self):
        def getMoreInfo(lst):
            result = ""
            for i in lst:
                result +=  f"{i[0]}\n{i[1]}"
            return result

        # 获取输入文本
        inputText = self.plainTextEdit.toPlainText()
        result = connect(inputText, from_language=self.fromLanguage)

        # 把结果放入到两个文本框中
        self.plainTextEdit_2.setPlainText(result["trans"])
        self.plainTextEdit_3.setPlainText(getMoreInfo(result["web"]))



if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()