# Form implementation generated from reading ui file 'AboutWindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgAbout(object):
    def setupUi(self, dlgAbout):
        dlgAbout.setObjectName("dlgAbout")
        dlgAbout.resize(391, 267)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/driver.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgAbout.setWindowIcon(icon)
        self.lblAutor = QtWidgets.QLabel(parent=dlgAbout)
        self.lblAutor.setGeometry(QtCore.QRect(10, 250, 97, 16))
        self.lblAutor.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lblAutor.setObjectName("lblAutor")
        self.frame = QtWidgets.QFrame(parent=dlgAbout)
        self.frame.setGeometry(QtCore.QRect(180, 20, 191, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lblVersion = QtWidgets.QLabel(parent=self.frame)
        self.lblVersion.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.lblVersion.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.lblVersion.setObjectName("lblVersion")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=dlgAbout)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 121, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/driver.ico"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=dlgAbout)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 251, 51))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(dlgAbout)
        QtCore.QMetaObject.connectSlotsByName(dlgAbout)

    def retranslateUi(self, dlgAbout):
        _translate = QtCore.QCoreApplication.translate
        dlgAbout.setWindowTitle(_translate("dlgAbout", "CarTeis"))
        self.lblAutor.setText(_translate("dlgAbout", "Brais Díaz Rodríguez"))
        self.lblVersion.setText(_translate("dlgAbout", "Versión 0.1"))
        self.label.setText(_translate("dlgAbout", "CarTeis"))
        self.label_3.setText(_translate("dlgAbout", "Aplicación dedicada al alquiler de coches por parte de ususarios."))
