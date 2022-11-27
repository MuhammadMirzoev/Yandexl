from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(399, 266)
        self.Do = QtWidgets.QPushButton(Form)
        self.Do.setGeometry(QtCore.QRect(40, 50, 81, 26))
        self.Do.setObjectName("Do")
        self.Re = QtWidgets.QPushButton(Form)
        self.Re.setGeometry(QtCore.QRect(160, 20, 81, 26))
        self.Re.setObjectName("Re")
        self.Mi = QtWidgets.QPushButton(Form)
        self.Mi.setGeometry(QtCore.QRect(260, 50, 81, 26))
        self.Mi.setObjectName("Mi")
        self.Fa = QtWidgets.QPushButton(Form)
        self.Fa.setGeometry(QtCore.QRect(280, 100, 81, 21))
        self.Fa.setObjectName("Fa")
        self.Sol = QtWidgets.QPushButton(Form)
        self.Sol.setGeometry(QtCore.QRect(10, 100, 81, 26))
        self.Sol.setObjectName("Sol")
        self.La = QtWidgets.QPushButton(Form)
        self.La.setGeometry(QtCore.QRect(40, 150, 81, 26))
        self.La.setObjectName("La")
        self.Ci = QtWidgets.QPushButton(Form)
        self.Ci.setGeometry(QtCore.QRect(260, 140, 81, 26))
        self.Ci.setObjectName("Ci")
        self.All = QtWidgets.QPushButton(Form)
        self.All.setGeometry(QtCore.QRect(150, 100, 91, 21))
        self.All.setObjectName("All")
        self.Do_2 = QtWidgets.QPushButton(Form)
        self.Do_2.setGeometry(QtCore.QRect(130, 170, 161, 71))
        self.Do_2.setObjectName("Do_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Do.setText(_translate("Form", "До"))
        self.Re.setText(_translate("Form", "Ре"))
        self.Mi.setText(_translate("Form", "Ми"))
        self.Fa.setText(_translate("Form", "Фа"))
        self.Sol.setText(_translate("Form", "Соль"))
        self.La.setText(_translate("Form", "Ля"))
        self.Ci.setText(_translate("Form", "Си"))
        self.All.setText(_translate("Form", "Все разом"))
        self.Do_2.setText(_translate("Form", "До во второй октаве"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
