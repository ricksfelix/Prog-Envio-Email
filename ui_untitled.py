# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledQwkWKJ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(607, 460)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"	background-color: #0E84FC;\n"
"	color: #fff;\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPushButton:focus {\n"
"	background-color: #015EBD;\n"
"	outline: none;\n"
"}\n"
"QCheckBox {\n"
"	color: #fff;\n"
"	font: 500 11pt \"Montserrat SemiBold\";\n"
"}\n"
"QCheckBox::hover {\n"
"	color: #0e84fc;\n"
"	font: 500 11pt \"Montserrat SemiBold\";\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: #015EBD;\n"
"}\n"
"QProgressBar::chunk  {\n"
"	color: #fff;\n"
"	background-color: #015EBD;\n"
"}\n"
"QToolButton {\n"
"	color: #fff;\n"
"}\n"
"QLabel {\n"
"	color: #fff;\n"
"	font: 600 10pt \"Montserrat SemiBold\";\n"
"}\n"
"QLabel::hover {\n"
"	color: #015EBD;\n"
"}\n"
"QLineEdit {\n"
"	border-radius: 5px;\n"
"	padding: 5px  5px  7px  8px ;\n"
"	border: 1px solid #353535;\n"
"	font: 600 9pt \"Montserrat SemiBold\";\n"
"}\n"
"QRadioButton {\n"
"	color: #fff;\n"
"	font: 600 10pt \"Montserrat SemiBold\";\n"
"}\n"
"QRadioButton::hover {\n"
"	color: #015EBD;\n"
"}\n"
"QComboBox {\n"
"	color: #000"
                        ";\n"
"	font: 600 11pt \"Montserrat SemiBold\";\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QComboBox::drop-down {\n"
"	margin: -3px 5px 7px -40px;\n"
"	border-radius: 0px;\n"
"	background-image: url(:/newPrefix/down.png);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color:  #353535;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.horizontalSpacer = QSpacerItem(179, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        font = QFont()
        font.setPointSize(16)
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"	color: #fff;\n"
"	font: 600 14pt \"Montserrat SemiBold\";\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_5)

        self.horizontalSpacer_2 = QSpacerItem(179, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color:  #353535;\n"
"}\n"
"QTextEdit {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"	padding: 5px  5px  7px  8px ;\n"
"	border: 1px solid #353535;\n"
"	font: 600 9pt \"Montserrat SemiBold\";\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.le_dest = QLineEdit(self.frame_3)
        self.le_dest.setObjectName(u"le_dest")
        self.le_dest.setMaxLength(64)

        self.verticalLayout_3.addWidget(self.le_dest)

        self.le_title = QLineEdit(self.frame_3)
        self.le_title.setObjectName(u"le_title")
        self.le_title.setMaxLength(64)

        self.verticalLayout_3.addWidget(self.le_title)

        self.le_text = QTextEdit(self.frame_3)
        self.le_text.setObjectName(u"le_text")
        self.le_text.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.le_text)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.le_email = QLineEdit(self.frame_4)
        self.le_email.setObjectName(u"le_email")
        self.le_email.setMaxLength(64)

        self.verticalLayout_2.addWidget(self.le_email)

        self.le_smtp = QLineEdit(self.frame_4)
        self.le_smtp.setObjectName(u"le_smtp")
        self.le_smtp.setMaxLength(64)

        self.verticalLayout_2.addWidget(self.le_smtp)

        self.le_passwd = QLineEdit(self.frame_4)
        self.le_passwd.setObjectName(u"le_passwd")
        self.le_passwd.setMaxLength(64)
        self.le_passwd.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.le_passwd)

        self.le_port = QLineEdit(self.frame_4)
        self.le_port.setObjectName(u"le_port")
        self.le_port.setMaxLength(5)

        self.verticalLayout_2.addWidget(self.le_port)

        self.cb_ssl = QCheckBox(self.frame_4)
        self.cb_ssl.setObjectName(u"cb_ssl")
        self.cb_ssl.setChecked(False)

        self.verticalLayout_2.addWidget(self.cb_ssl)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setStyleSheet(u"QFrame {\n"
"	background-color:  #353535;\n"
"}\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(30, 30, 30, 30)
        self.lb_result = QLabel(self.frame_6)
        self.lb_result.setObjectName(u"lb_result")
        self.lb_result.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lb_result)

        self.bt_send = QPushButton(self.frame_6)
        self.bt_send.setObjectName(u"bt_send")

        self.verticalLayout_5.addWidget(self.bt_send)


        self.verticalLayout_4.addWidget(self.frame_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Prog envio de e-mail", None))
        self.le_dest.setText("")
        self.le_dest.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Destinatario", None))
        self.le_title.setText("")
        self.le_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Assunto", None))
        self.le_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Montserrat SemiBold'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-weight:400;\"><br /></p></body></html>", None))
        self.le_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Corpo do email", None))
        self.le_email.setText("")
        self.le_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.le_smtp.setText("")
        self.le_smtp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Servidor SMTP", None))
        self.le_passwd.setText("")
        self.le_passwd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.le_port.setText("")
        self.le_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Porta", None))
        self.cb_ssl.setText(QCoreApplication.translate("MainWindow", u"Utiliza SSL", None))
        self.lb_result.setText("")
        self.bt_send.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi

