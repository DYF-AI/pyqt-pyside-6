
from PySide6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()
        # # 设置水平滑条
        # slider1 = QSlider(Qt.Orientation.Horizontal)
        # # 设置刻度位置
        # slider1.setTickPosition(QSlider.TickPosition.TicksBelow)
        # # 设置刻度间隔, j间隔越大下面的刻度越小
        # slider1.setTickInterval(5)
        # # 设置最小值和最大值
        # slider1.setMinimum(50)
        # slider1.setMaximum(150)
        #
        # slider1.valueChanged.connect(self.showSlider)
        # mainLayout.addWidget(slider1)

        slider = QSlider(Qt.Orientation.Horizontal)
        # slider.setMinimum(0)
        # slider.setMaximum(100)
        slider.setRange(0,100)

        slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider.setTickInterval(5)
        slider.valueChanged.connect(self.showSlider)
        mainLayout.addWidget(slider)

        self.setLayout(mainLayout)

    def showSlider(self, value):
        # current_widget = self.sender()
        # print(current_widget.value())
        print(f"滑条当前的值为:{value}")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()