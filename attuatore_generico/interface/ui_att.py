from PyQt5 import QtCore, QtWidgets
from qtwidgets.toggle.toggle import AnimatedToggle

'''
    Implementazione della classe Ui_Att
    
    Definisce un'interfaccia per la gui di un attuatore generico
'''

class Ui_Att():
    
    '''
        Costruisce la gui
        Parametri:
            (attuatore_generico.interface.vista_att) vista dell'attuatore
    '''

    def setup_ui(self, att):
        att.setObjectName("att")
        att.resize(960, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(att.sizePolicy().hasHeightForWidth())
        att.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(att)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.data_ora = QtWidgets.QLabel(att)
        self.data_ora.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.data_ora.setObjectName("data_ora")
        self.horizontalLayout_1.addWidget(self.data_ora)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem)
        self.horizontalLayout_1.setStretch(0, 28)
        self.horizontalLayout_1.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.consumo_medio = QtWidgets.QLabel(att)
        self.consumo_medio.setObjectName("consumo_medio")
        self.horizontalLayout_9.addWidget(self.consumo_medio)
        self.valore_medio = QtWidgets.QLabel(att)
        self.valore_medio.setObjectName("valore_medio")
        self.horizontalLayout_9.addWidget(self.valore_medio)
        self.gridLayout.addLayout(self.horizontalLayout_9, 9, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.elettricita = QtWidgets.QLabel(att)
        self.elettricita.setObjectName("elettricita")
        self.horizontalLayout_7.addWidget(self.elettricita)
        self.gridLayout.addLayout(self.horizontalLayout_7, 7, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 10, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(1, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.titolo = QtWidgets.QLabel(att)
        self.titolo.setObjectName("titolo")
        self.horizontalLayout_3.addWidget(self.titolo)
        self.onoff_att = AnimatedToggle(checked_color="#00ff00",pulse_checked_color = "#00ff00")
        self.onoff_att.setObjectName("onoff_att")
        self.horizontalLayout_3.addWidget(self.onoff_att)
        self.horizontalLayout_3.addStretch()
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2,4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.obiettivo = QtWidgets.QLabel(att)
        self.obiettivo.setObjectName("obiettivo")
        self.horizontalLayout_5.addWidget(self.obiettivo)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.spinBox = QtWidgets.QSpinBox(att)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_5.addWidget(self.spinBox)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.horizontalLayout_5.setStretch(0, 20)
        self.horizontalLayout_5.setStretch(1, 10)
        self.horizontalLayout_5.setStretch(2, 20)
        self.horizontalLayout_5.setStretch(3, 20)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.suggerimento = QtWidgets.QLabel(att)
        self.suggerimento.setObjectName("suggerimento")
        self.horizontalLayout_6.addWidget(self.suggerimento)
        self.nome_coltura = QtWidgets.QLabel(att)
        self.nome_coltura.setObjectName("nome_coltura")
        self.horizontalLayout_6.addWidget(self.nome_coltura)
        self.e_label = QtWidgets.QLabel(att)
        self.e_label.setObjectName("e_label")
        self.horizontalLayout_6.addWidget(self.e_label)
        self.valore_consigliato = QtWidgets.QLabel(att)
        self.valore_consigliato.setObjectName("valore_consigliato")
        self.horizontalLayout_6.addWidget(self.valore_consigliato)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.consumo_corrente = QtWidgets.QLabel(att)
        self.consumo_corrente.setObjectName("consumo_corrente")
        self.horizontalLayout_8.addWidget(self.consumo_corrente)
        self.valore_corrente = QtWidgets.QLabel(att)
        self.valore_corrente.setObjectName("valore_corrente")
        self.horizontalLayout_8.addWidget(self.valore_corrente)
        self.gridLayout.addLayout(self.horizontalLayout_8, 8, 1, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 10)
        self.gridLayout.setColumnMinimumWidth(1, 10)
        self.gridLayout.setColumnMinimumWidth(2, 10)
        self.gridLayout.setRowMinimumHeight(0, 20)
        self.gridLayout.setRowMinimumHeight(1, 20)
        self.gridLayout.setRowMinimumHeight(2, 20)
        self.gridLayout.setRowMinimumHeight(3, 20)
        self.gridLayout.setRowMinimumHeight(4, 20)
        self.gridLayout.setRowMinimumHeight(5, 20)
        self.gridLayout.setRowMinimumHeight(6, 20)
        self.gridLayout.setRowMinimumHeight(7, 20)
        self.gridLayout.setRowMinimumHeight(8, 20)
        self.gridLayout.setRowMinimumHeight(9, 20)
        self.gridLayout.setRowMinimumHeight(10, 20)
        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setColumnStretch(1, 20)
        self.gridLayout.setColumnStretch(2, 20)
        self.gridLayout.setRowStretch(2, 10)
        self.gridLayout.setRowStretch(3, 15)
        self.gridLayout.setRowStretch(4, 10)
        self.gridLayout.setRowStretch(5, 10)
        self.gridLayout.setRowStretch(6, 20)
        self.gridLayout.setRowStretch(7, 10)
        self.gridLayout.setRowStretch(8, 10)
        self.gridLayout.setRowStretch(9, 10)
        self.gridLayout.setRowStretch(10, 10)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.indietro = QtWidgets.QPushButton(att)
        self.indietro.setObjectName("indietro")
        self.horizontalLayout_2.addWidget(self.indietro)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 12)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 24)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(att)
        QtCore.QMetaObject.connectSlotsByName(att)