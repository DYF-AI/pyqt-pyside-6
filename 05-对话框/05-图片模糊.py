from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QPushButton,QFileDialog
from PySide6.QtCore import Qt
from PIL import ImageQt, Image, ImageFilter
from PySide6.QtGui import QPixmap

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.img = None
        self.btn = QPushButton("点我导入图像")
        self.btn.clicked.connect(self.getImage)

        self.lbShowImage = QLabel()

        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(0, 20)
        slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider.setTickInterval(3)
        slider.valueChanged.connect(self.sliderBlurChange)

        #self.pic = Image.open("20231216204952.jpg")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.btn)
        self.mainLayout.addWidget(self.lbShowImage)
        self.mainLayout.addWidget(slider)
        self.setLayout(self.mainLayout)

    def sliderBlurChange(self, value):
        blurImg = self.img.filter(ImageFilter.GaussianBlur(value))
        self.lbShowImage.setPixmap(ImageQt.toqpixmap(blurImg))

    def getImage(self):
        self.img = Image.open(QFileDialog.getOpenFileName(self, "选择图像", "./", "图像文件(*.png *.jpg)")[0])
        self.lbShowImage.setPixmap(ImageQt.toqpixmap(self.img))

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
