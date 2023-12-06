from PySide6.QtWidgets import QApplication, QWidget
from ui_trans import Ui_Form


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 用于储存数据类型的字典
        self.lengthVar = {"米": 100, "厘米": 1, "千米": 100000, "分米": 10}
        self.weightVar = {"克": 1, "千克": 1000, "斤": 500}

        self.TypeDict = {"长度": self.lengthVar, "质量": self.weightVar}

        self.dataTypeComboBox.addItems(self.TypeDict.keys())
        self.oneInputComboBox.addItems(self.lengthVar.keys())
        self.twoInputComboBox.addItems(self.lengthVar.keys())

        self.bind()

    def bind(self):
        self.dataTypeComboBox.currentTextChanged.connect(self.typeChange)
        self.calcBtn.clicked.connect(self.calc)

    def calc(self):
        bigType = self.dataTypeComboBox.currentText()
        # 获取第一个输入框的值
        value = self.oneInputEditLine.text()
        if value == "":
            return
        currentType = self.oneInputComboBox.currentText()
        transType = self.twoInputComboBox.currentText()

        standardization = float(value) * self.TypeDict[bigType][currentType]
        result = standardization / self.TypeDict[bigType][transType]

        self.originDataLabel.setText(f"{value} {currentType} =")
        self.transDataLabel.setText(f"{result} {transType}")
        self.twoInputEditLine.setText(str(result))


    def typeChange(self, text):
        self.oneInputComboBox.clear()
        self.twoInputComboBox.clear()

        self.oneInputComboBox.addItems(self.TypeDict[text].keys())
        self.twoInputComboBox.addItems(self.TypeDict[text].keys())



if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
