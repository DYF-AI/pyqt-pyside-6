# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'translate.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1270, 711)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 281, 71))
        self.groupBox.setCheckable(False)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 271, 21))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u".QComboBox{\n"
"	border-radius:10%;\n"
"	borden:1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius:10%;\n"
"	borden:1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}")

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(20, 80, 281, 151))
        self.plainTextEdit.setStyleSheet(u".QComboBox{\n"
"	border-radius:10%;\n"
"	borden:1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius:10%;\n"
"	borden:1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}")
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(310, 20, 261, 22))
        self.comboBox.setStyleSheet(u".QComboBox{\n"
"	border-radius:10%;\n"
"	borden:1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius:10%;\n"
"	borden:1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}")
        self.comboBox.setEditable(True)
        self.plainTextEdit_2 = QPlainTextEdit(Form)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(310, 50, 261, 201))
        self.plainTextEdit_2.setStyleSheet(u".QComboBox{\n"
"	border-radius:10%;\n"
"	borden:1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius:10%;\n"
"	borden:1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}")
        self.plainTextEdit_3 = QPlainTextEdit(Form)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(20, 260, 551, 91))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 230, 281, 23))
        self.pushButton.setStyleSheet(u".QComboBox{\n"
"	border-radius:10%;\n"
"	borden:1px solid black;\n"
"}\n"
"\n"
".QLineEdit{\n"
"	border-radius:10%;\n"
"	borden:1px solid black;\n"
"}\n"
"\n"
".QComboBox:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}\n"
"\n"
".QLineEdit:hover{\n"
"	background-color:rgb(170,255,255);\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7ffb\u8bd1\u5728\u7ebf", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u8f93\u5165\u8bed\u8a00", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u8bc6\u522b", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u6c49\u8bed", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u82f1\u8bed", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u6c49\u8bed", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u65e5\u8bed", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u8f93\u51fa\u8bed\u8a00", None))
        self.plainTextEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u663e\u793a\u66f4\u591a", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u7ffb\u8bd1", None))
    # retranslateUi

