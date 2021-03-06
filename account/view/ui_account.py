from PyQt5 import QtCore, QtWidgets

'''
    Implementazione della classe Ui_Account
    Crea la gui della vista Account
'''

class Ui_Account(object):

    '''
        Crea la gui
    '''

    def setup_ui(self, layout_base):
        layout_base.setObjectName("layout_base")
        layout_base.resize(960, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(layout_base.sizePolicy().hasHeightForWidth())
        layout_base.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(layout_base)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.data_ora = QtWidgets.QLabel(layout_base)
        self.data_ora.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.data_ora.setObjectName("data_ora")
        self.horizontalLayout_1.addWidget(self.data_ora)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem)
        self.horizontalLayout_1.setStretch(0, 28)
        self.horizontalLayout_1.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(layout_base)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.modifica_username = QtWidgets.QLabel(layout_base)
        self.modifica_username.setObjectName("modifica_username")
        self.gridLayout_2.addWidget(self.modifica_username, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        self.gridLayout_2.setRowMinimumHeight(0, 10)
        self.gridLayout_2.setRowMinimumHeight(1, 10)
        self.gridLayout_2.setRowMinimumHeight(2, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 100)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.label_errore_1 = QtWidgets.QLabel(layout_base)
        self.label_errore_1.setIndent(30)
        self.label_errore_1.setObjectName("label_errore_1")
        self.verticalLayout_3.addWidget(self.label_errore_1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.username_field = QtWidgets.QLineEdit(layout_base)
        self.username_field.setObjectName("username_field")
        self.verticalLayout_4.addWidget(self.username_field)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.applica_modifiche = QtWidgets.QPushButton(layout_base)
        self.applica_modifiche.setObjectName("applica_modifiche")
        self.horizontalLayout_11.addWidget(self.applica_modifiche)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.horizontalLayout_11.setStretch(0, 100)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 100)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.setStretch(0, 10)
        self.verticalLayout_4.setStretch(1, 10)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_5.setStretch(0, 10)
        self.horizontalLayout_5.setStretch(1, 7)
        self.horizontalLayout_5.setStretch(2, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 2, 1, 1)
        self.modifica_password = QtWidgets.QLabel(layout_base)
        self.modifica_password.setObjectName("modifica_password")
        self.gridLayout_3.addWidget(self.modifica_password, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(layout_base)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem10, 2, 1, 1, 1)
        self.gridLayout_3.setRowMinimumHeight(0, 10)
        self.gridLayout_3.setRowMinimumHeight(1, 10)
        self.gridLayout_3.setRowMinimumHeight(2, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 100)
        self.horizontalLayout_6.addLayout(self.gridLayout_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.label_errore_2 = QtWidgets.QLabel(layout_base)
        self.label_errore_2.setIndent(30)
        self.label_errore_2.setObjectName("label_errore_2")
        self.verticalLayout_3.addWidget(self.label_errore_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(layout_base)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 0, 2, 1, 1)
        self.vecchia_password = QtWidgets.QLabel(layout_base)
        self.vecchia_password.setObjectName("vecchia_password")
        self.gridLayout.addWidget(self.vecchia_password, 0, 1, 1, 1)
        self.nuova_password = QtWidgets.QLabel(layout_base)
        self.nuova_password.setObjectName("nuova_password")
        self.gridLayout.addWidget(self.nuova_password, 1, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.nuova_password_field = QtWidgets.QLineEdit(layout_base)
        self.nuova_password_field.setObjectName("nuova_password_field")
        self.nuova_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_9.addWidget(self.nuova_password_field)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.horizontalLayout_9.setStretch(0, 100)
        self.horizontalLayout_9.setStretch(1, 145)
        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 3, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.conferma_password_field = QtWidgets.QLineEdit(layout_base)
        self.conferma_password_field.setObjectName("conferma_password_field")
        self.conferma_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_10.addWidget(self.conferma_password_field)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem14)
        self.horizontalLayout_10.setStretch(0, 100)
        self.horizontalLayout_10.setStretch(1, 145)
        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 3, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.vecchia_password_field = QtWidgets.QLineEdit(layout_base)
        self.vecchia_password_field.setObjectName("vecchia_password_field")
        self.vecchia_password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_8.addWidget(self.vecchia_password_field)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        self.horizontalLayout_8.setStretch(0, 100)
        self.horizontalLayout_8.setStretch(1, 145)
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.applica_modifiche_2 = QtWidgets.QPushButton(layout_base)
        self.applica_modifiche_2.setObjectName("applica_modifiche_2")
        self.horizontalLayout.addWidget(self.applica_modifiche_2)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem17)
        self.horizontalLayout.setStretch(0, 40)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 229)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 3, 1, 1)
        self.gridLayout.setColumnStretch(0, 20)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 10)
        self.gridLayout.setColumnStretch(3, 110)
        self.verticalLayout_3.addLayout(self.gridLayout)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem18)
        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(2, 10)
        self.verticalLayout_3.setStretch(3, 10)
        self.verticalLayout_3.setStretch(4, 10)
        self.verticalLayout_3.setStretch(6, 30)
        self.verticalLayout_3.setStretch(7, 10)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem19)
        self.indietro = QtWidgets.QPushButton(layout_base)
        self.indietro.setObjectName("indietro")
        self.horizontalLayout_2.addWidget(self.indietro)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem20)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 12)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 24)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(layout_base)
        QtCore.QMetaObject.connectSlotsByName(layout_base)

    '''
        Setta i testi nella view
    '''

    def retranslateUi(self, ui):
        _translate = QtCore.QCoreApplication.translate
        ui.setWindowTitle(_translate("ui", "GreenExperience"))
        self.data_ora.setText(_translate("ui", "DATA/ORA"))
        self.modifica_username.setText(_translate("ui", "Modifica username"))
        self.applica_modifiche.setText(_translate("ui", "applica modifiche"))
        self.modifica_password.setText(_translate("ui", "Modifica password"))
        self.label_5.setText(_translate("ui", "conferma nuova password"))
        self.vecchia_password.setText(_translate("ui", "vecchia password"))
        self.nuova_password.setText(_translate("ui", "nuova password"))
        self.applica_modifiche_2.setText(_translate("ui", "applica modifiche"))
        self.label_errore_1.setText(_translate("ui", ""))
        self.label_errore_2.setText(_translate("ui", ""))
        self.indietro.setText(_translate("ui", "Indietro"))