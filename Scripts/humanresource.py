# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hr.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1018, 762)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(13)
        self.verticalLayout.setObjectName("verticalLayout")
        self.myTab = QtWidgets.QTabWidget(Dialog)
        font = QtGui.QFont()
        font.setKerning(True)
        self.myTab.setFont(font)
        self.myTab.setTabPosition(QtWidgets.QTabWidget.North)
        self.myTab.setIconSize(QtCore.QSize(40, 40))
        self.myTab.setElideMode(QtCore.Qt.ElideNone)
        self.myTab.setObjectName("myTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.cwHome = QtWidgets.QCalendarWidget(self.tab)
        self.cwHome.setGeometry(QtCore.QRect(510, 270, 471, 431))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.cwHome.setFont(font)
        self.cwHome.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.cwHome.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.cwHome.setNavigationBarVisible(True)
        self.cwHome.setDateEditEnabled(True)
        self.cwHome.setObjectName("cwHome")
        self.lblProfileHome = QtWidgets.QLabel(self.tab)
        self.lblProfileHome.setGeometry(QtCore.QRect(30, 40, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblProfileHome.setFont(font)
        self.lblProfileHome.setText("")
        self.lblProfileHome.setPixmap(QtGui.QPixmap("../../../../../PycharmProjects/pythonProject/images/man.png"))
        self.lblProfileHome.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProfileHome.setObjectName("lblProfileHome")
        self.label_34 = QtWidgets.QLabel(self.tab)
        self.label_34.setGeometry(QtCore.QRect(180, 50, 67, 17))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.tab)
        self.label_35.setGeometry(QtCore.QRect(180, 90, 67, 17))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab)
        self.label_36.setGeometry(QtCore.QRect(180, 130, 67, 17))
        self.label_36.setObjectName("label_36")
        self.lblNameHome = QtWidgets.QLabel(self.tab)
        self.lblNameHome.setGeometry(QtCore.QRect(280, 50, 67, 17))
        self.lblNameHome.setObjectName("lblNameHome")
        self.lblSurnameHome = QtWidgets.QLabel(self.tab)
        self.lblSurnameHome.setGeometry(QtCore.QRect(280, 90, 67, 17))
        self.lblSurnameHome.setObjectName("lblSurnameHome")
        self.lblTelHome = QtWidgets.QLabel(self.tab)
        self.lblTelHome.setGeometry(QtCore.QRect(280, 130, 121, 17))
        self.lblTelHome.setObjectName("lblTelHome")
        self.label_40 = QtWidgets.QLabel(self.tab)
        self.label_40.setGeometry(QtCore.QRect(180, 160, 67, 17))
        self.label_40.setObjectName("label_40")
        self.lblEmailHome = QtWidgets.QLabel(self.tab)
        self.lblEmailHome.setGeometry(QtCore.QRect(280, 160, 231, 17))
        self.lblEmailHome.setObjectName("lblEmailHome")
        self.lblLogoHome = QtWidgets.QLabel(self.tab)
        self.lblLogoHome.setGeometry(QtCore.QRect(620, 0, 261, 271))
        self.lblLogoHome.setText("")
        self.lblLogoHome.setPixmap(QtGui.QPixmap("../../../../../PycharmProjects/pythonProject/images/version2.0.png"))
        self.lblLogoHome.setObjectName("lblLogoHome")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 200, 351, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(60)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnFullProfileHome = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFullProfileHome.sizePolicy().hasHeightForWidth())
        self.btnFullProfileHome.setSizePolicy(sizePolicy)
        self.btnFullProfileHome.setObjectName("btnFullProfileHome")
        self.horizontalLayout_5.addWidget(self.btnFullProfileHome)
        self.btnUpdateProfileHome = QtWidgets.QPushButton(self.layoutWidget)
        self.btnUpdateProfileHome.setObjectName("btnUpdateProfileHome")
        self.horizontalLayout_5.addWidget(self.btnUpdateProfileHome)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 271, 353, 431))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_32 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_5.addWidget(self.label_32)
        self.lwTimeTableHome = QtWidgets.QListWidget(self.layoutWidget1)
        self.lwTimeTableHome.setObjectName("lwTimeTableHome")
        self.verticalLayout_5.addWidget(self.lwTimeTableHome)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnAddHome = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnAddHome.setObjectName("btnAddHome")
        self.horizontalLayout_6.addWidget(self.btnAddHome)
        self.btnDeleteHome = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnDeleteHome.setObjectName("btnDeleteHome")
        self.horizontalLayout_6.addWidget(self.btnDeleteHome)
        self.btnDeleteAllHome = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnDeleteAllHome.setObjectName("btnDeleteAllHome")
        self.horizontalLayout_6.addWidget(self.btnDeleteAllHome)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.myTab.addTab(self.tab, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_7)
        self.layoutWidget2.setGeometry(QtCore.QRect(480, 11, 441, 691))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.cmbPositionShowProfiles = QtWidgets.QComboBox(self.layoutWidget2)
        self.cmbPositionShowProfiles.setObjectName("cmbPositionShowProfiles")
        self.horizontalLayout_3.addWidget(self.cmbPositionShowProfiles)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(13)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnShowAllShowProfiles = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnShowAllShowProfiles.setObjectName("btnShowAllShowProfiles")
        self.horizontalLayout_2.addWidget(self.btnShowAllShowProfiles)
        self.btnSearchByIdShowProfiles = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnSearchByIdShowProfiles.setObjectName("btnSearchByIdShowProfiles")
        self.horizontalLayout_2.addWidget(self.btnSearchByIdShowProfiles)
        self.btnSearchByNameShowProfiles = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnSearchByNameShowProfiles.setObjectName("btnSearchByNameShowProfiles")
        self.horizontalLayout_2.addWidget(self.btnSearchByNameShowProfiles)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.lwShowProfiles = QtWidgets.QListWidget(self.layoutWidget2)
        self.lwShowProfiles.setObjectName("lwShowProfiles")
        self.gridLayout_2.addWidget(self.lwShowProfiles, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(13)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnNewShowProfiles = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnNewShowProfiles.setObjectName("btnNewShowProfiles")
        self.horizontalLayout_4.addWidget(self.btnNewShowProfiles)
        self.btnUpdateShowProfiles = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnUpdateShowProfiles.setObjectName("btnUpdateShowProfiles")
        self.horizontalLayout_4.addWidget(self.btnUpdateShowProfiles)
        self.btnDeleteShowProfiles = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnDeleteShowProfiles.setObjectName("btnDeleteShowProfiles")
        self.horizontalLayout_4.addWidget(self.btnDeleteShowProfiles)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_7)
        self.layoutWidget3.setGeometry(QtCore.QRect(50, 280, 421, 381))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblAddressShowProfiles = QtWidgets.QLabel(self.layoutWidget3)
        self.lblAddressShowProfiles.setObjectName("lblAddressShowProfiles")
        self.gridLayout_3.addWidget(self.lblAddressShowProfiles, 5, 1, 1, 1)
        self.lblPhoneShowProfiles = QtWidgets.QLabel(self.layoutWidget3)
        self.lblPhoneShowProfiles.setObjectName("lblPhoneShowProfiles")
        self.gridLayout_3.addWidget(self.lblPhoneShowProfiles, 3, 1, 1, 1)
        self.lblNameShowProfiles = QtWidgets.QLabel(self.layoutWidget3)
        self.lblNameShowProfiles.setObjectName("lblNameShowProfiles")
        self.gridLayout_3.addWidget(self.lblNameShowProfiles, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 4, 0, 1, 1)
        self.lblSurnameShowProfiles = QtWidgets.QLabel(self.layoutWidget3)
        self.lblSurnameShowProfiles.setObjectName("lblSurnameShowProfiles")
        self.gridLayout_3.addWidget(self.lblSurnameShowProfiles, 2, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.lblEmailShowProfiles = QtWidgets.QLabel(self.layoutWidget3)
        self.lblEmailShowProfiles.setObjectName("lblEmailShowProfiles")
        self.gridLayout_3.addWidget(self.lblEmailShowProfiles, 4, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1)
        self.lblIdentityShowProfiles = QtWidgets.QLabel(self.layoutWidget3)
        self.lblIdentityShowProfiles.setObjectName("lblIdentityShowProfiles")
        self.gridLayout_3.addWidget(self.lblIdentityShowProfiles, 0, 1, 1, 1)
        self.layoutWidget4 = QtWidgets.QWidget(self.tab_7)
        self.layoutWidget4.setGeometry(QtCore.QRect(110, 40, 291, 221))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.lblProfileShowProfiles = QtWidgets.QLabel(self.layoutWidget4)
        self.lblProfileShowProfiles.setText("")
        self.lblProfileShowProfiles.setPixmap(QtGui.QPixmap("../../../../../../PycharmProjects/pythonProject/images/employee12.png"))
        self.lblProfileShowProfiles.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProfileShowProfiles.setObjectName("lblProfileShowProfiles")
        self.verticalLayout_3.addWidget(self.lblProfileShowProfiles)
        self.myTab.addTab(self.tab_7, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label = QtWidgets.QLabel(self.tab_6)
        self.label.setGeometry(QtCore.QRect(410, 0, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_6)
        self.label_2.setGeometry(QtCore.QRect(440, 60, 121, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../../PycharmProjects/pythonProject/images/man.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_6)
        self.label_3.setGeometry(QtCore.QRect(100, 210, 67, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_6)
        self.label_4.setGeometry(QtCore.QRect(100, 300, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_6)
        self.label_5.setGeometry(QtCore.QRect(100, 380, 67, 17))
        self.label_5.setObjectName("label_5")
        self.lnIdAddPersonel = QtWidgets.QLineEdit(self.tab_6)
        self.lnIdAddPersonel.setGeometry(QtCore.QRect(100, 240, 261, 31))
        self.lnIdAddPersonel.setObjectName("lnIdAddPersonel")
        self.lnNameAddPersonel = QtWidgets.QLineEdit(self.tab_6)
        self.lnNameAddPersonel.setGeometry(QtCore.QRect(100, 320, 261, 31))
        self.lnNameAddPersonel.setObjectName("lnNameAddPersonel")
        self.lnSurnameAddPersonel = QtWidgets.QLineEdit(self.tab_6)
        self.lnSurnameAddPersonel.setGeometry(QtCore.QRect(100, 400, 261, 31))
        self.lnSurnameAddPersonel.setObjectName("lnSurnameAddPersonel")
        self.label_6 = QtWidgets.QLabel(self.tab_6)
        self.label_6.setGeometry(QtCore.QRect(100, 460, 67, 17))
        self.label_6.setObjectName("label_6")
        self.lnPhoneAddPersonel = QtWidgets.QLineEdit(self.tab_6)
        self.lnPhoneAddPersonel.setGeometry(QtCore.QRect(100, 480, 261, 31))
        self.lnPhoneAddPersonel.setObjectName("lnPhoneAddPersonel")
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        self.label_7.setGeometry(QtCore.QRect(100, 540, 67, 17))
        self.label_7.setObjectName("label_7")
        self.lnEmailAddPersonel = QtWidgets.QLineEdit(self.tab_6)
        self.lnEmailAddPersonel.setGeometry(QtCore.QRect(100, 560, 261, 31))
        self.lnEmailAddPersonel.setObjectName("lnEmailAddPersonel")
        self.lnSalaryAddPersonel = QtWidgets.QLineEdit(self.tab_6)
        self.lnSalaryAddPersonel.setGeometry(QtCore.QRect(630, 240, 261, 31))
        self.lnSalaryAddPersonel.setObjectName("lnSalaryAddPersonel")
        self.label_10 = QtWidgets.QLabel(self.tab_6)
        self.label_10.setGeometry(QtCore.QRect(630, 220, 67, 17))
        self.label_10.setObjectName("label_10")
        self.label_15 = QtWidgets.QLabel(self.tab_6)
        self.label_15.setGeometry(QtCore.QRect(630, 300, 67, 17))
        self.label_15.setObjectName("label_15")
        self.btnBrowseAddPersonel = QtWidgets.QPushButton(self.tab_6)
        self.btnBrowseAddPersonel.setGeometry(QtCore.QRect(100, 640, 261, 31))
        self.btnBrowseAddPersonel.setObjectName("btnBrowseAddPersonel")
        self.label_16 = QtWidgets.QLabel(self.tab_6)
        self.label_16.setGeometry(QtCore.QRect(100, 620, 67, 17))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_6)
        self.label_17.setGeometry(QtCore.QRect(630, 370, 67, 21))
        self.label_17.setObjectName("label_17")
        self.txtEditAddressAddPersonel = QtWidgets.QTextEdit(self.tab_6)
        self.txtEditAddressAddPersonel.setGeometry(QtCore.QRect(630, 400, 261, 181))
        self.txtEditAddressAddPersonel.setObjectName("txtEditAddressAddPersonel")
        self.btnAddAddPersonel = QtWidgets.QPushButton(self.tab_6)
        self.btnAddAddPersonel.setGeometry(QtCore.QRect(630, 590, 131, 31))
        self.btnAddAddPersonel.setObjectName("btnAddAddPersonel")
        self.cmbPositionAddPersonel = QtWidgets.QComboBox(self.tab_6)
        self.cmbPositionAddPersonel.setGeometry(QtCore.QRect(780, 590, 111, 31))
        self.cmbPositionAddPersonel.setObjectName("cmbPositionAddPersonel")
        self.label_18 = QtWidgets.QLabel(self.tab_6)
        self.label_18.setGeometry(QtCore.QRect(890, 240, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.btnClearAllAddPersonel = QtWidgets.QPushButton(self.tab_6)
        self.btnClearAllAddPersonel.setGeometry(QtCore.QRect(630, 640, 261, 31))
        self.btnClearAllAddPersonel.setObjectName("btnClearAllAddPersonel")
        self.layoutWidget5 = QtWidgets.QWidget(self.tab_6)
        self.layoutWidget5.setGeometry(QtCore.QRect(630, 320, 261, 31))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rdMaleAddPersonel = QtWidgets.QRadioButton(self.layoutWidget5)
        self.rdMaleAddPersonel.setObjectName("rdMaleAddPersonel")
        self.horizontalLayout.addWidget(self.rdMaleAddPersonel)
        self.rdFemaleAddPersonel = QtWidgets.QRadioButton(self.layoutWidget5)
        self.rdFemaleAddPersonel.setObjectName("rdFemaleAddPersonel")
        self.horizontalLayout.addWidget(self.rdFemaleAddPersonel)
        self.myTab.addTab(self.tab_6, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.lnIdDeletePersonel = QtWidgets.QLineEdit(self.tab_5)
        self.lnIdDeletePersonel.setGeometry(QtCore.QRect(310, 230, 351, 41))
        self.lnIdDeletePersonel.setObjectName("lnIdDeletePersonel")
        self.btnDeleteDeletePersonel = QtWidgets.QPushButton(self.tab_5)
        self.btnDeleteDeletePersonel.setGeometry(QtCore.QRect(510, 300, 151, 41))
        self.btnDeleteDeletePersonel.setObjectName("btnDeleteDeletePersonel")
        self.cmbIdDeletePersonel = QtWidgets.QComboBox(self.tab_5)
        self.cmbIdDeletePersonel.setGeometry(QtCore.QRect(310, 300, 161, 41))
        self.cmbIdDeletePersonel.setObjectName("cmbIdDeletePersonel")
        self.cmbIdDeletePersonel.addItem("")
        self.cmbIdDeletePersonel.addItem("")
        self.myTab.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lnIdUpdatePersonel = QtWidgets.QLineEdit(self.tab_2)
        self.lnIdUpdatePersonel.setGeometry(QtCore.QRect(340, 220, 151, 31))
        self.lnIdUpdatePersonel.setObjectName("lnIdUpdatePersonel")
        self.btnLoadUpdatePersonel = QtWidgets.QPushButton(self.tab_2)
        self.btnLoadUpdatePersonel.setGeometry(QtCore.QRect(500, 220, 71, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../PycharmProjects/pythonProject/images/icon1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLoadUpdatePersonel.setIcon(icon)
        self.btnLoadUpdatePersonel.setObjectName("btnLoadUpdatePersonel")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(120, 280, 91, 31))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(120, 370, 91, 31))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(520, 280, 91, 31))
        self.label_28.setObjectName("label_28")
        self.lnNameUpdatePersonel = QtWidgets.QLineEdit(self.tab_2)
        self.lnNameUpdatePersonel.setGeometry(QtCore.QRect(120, 310, 271, 41))
        self.lnNameUpdatePersonel.setObjectName("lnNameUpdatePersonel")
        self.lnSurnameUpdatePersonel = QtWidgets.QLineEdit(self.tab_2)
        self.lnSurnameUpdatePersonel.setGeometry(QtCore.QRect(120, 400, 271, 41))
        self.lnSurnameUpdatePersonel.setObjectName("lnSurnameUpdatePersonel")
        self.lnPhoneUpdatePersonel = QtWidgets.QLineEdit(self.tab_2)
        self.lnPhoneUpdatePersonel.setGeometry(QtCore.QRect(520, 310, 271, 41))
        self.lnPhoneUpdatePersonel.setObjectName("lnPhoneUpdatePersonel")
        self.lnEmailUpdatePersonel = QtWidgets.QLineEdit(self.tab_2)
        self.lnEmailUpdatePersonel.setGeometry(QtCore.QRect(520, 400, 271, 41))
        self.lnEmailUpdatePersonel.setObjectName("lnEmailUpdatePersonel")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(520, 370, 91, 31))
        self.label_30.setObjectName("label_30")
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(120, 470, 67, 21))
        self.label_29.setObjectName("label_29")
        self.btnBrowseUpdatePersonel = QtWidgets.QPushButton(self.tab_2)
        self.btnBrowseUpdatePersonel.setGeometry(QtCore.QRect(120, 500, 271, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../PycharmProjects/pythonProject/images/browse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBrowseUpdatePersonel.setIcon(icon1)
        self.btnBrowseUpdatePersonel.setObjectName("btnBrowseUpdatePersonel")
        self.label_31 = QtWidgets.QLabel(self.tab_2)
        self.label_31.setGeometry(QtCore.QRect(520, 470, 67, 21))
        self.label_31.setObjectName("label_31")
        self.txtEditAddressUpdatePersonel = QtWidgets.QTextEdit(self.tab_2)
        self.txtEditAddressUpdatePersonel.setGeometry(QtCore.QRect(520, 500, 271, 141))
        self.txtEditAddressUpdatePersonel.setObjectName("txtEditAddressUpdatePersonel")
        self.btnSaveUpdatePersonel = QtWidgets.QPushButton(self.tab_2)
        self.btnSaveUpdatePersonel.setGeometry(QtCore.QRect(520, 650, 121, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../../PycharmProjects/pythonProject/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSaveUpdatePersonel.setIcon(icon2)
        self.btnSaveUpdatePersonel.setObjectName("btnSaveUpdatePersonel")
        self.btnCancelUpdatePersonel = QtWidgets.QPushButton(self.tab_2)
        self.btnCancelUpdatePersonel.setGeometry(QtCore.QRect(670, 650, 121, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../../PycharmProjects/pythonProject/images/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelUpdatePersonel.setIcon(icon3)
        self.btnCancelUpdatePersonel.setObjectName("btnCancelUpdatePersonel")
        self.layoutWidget6 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget6.setGeometry(QtCore.QRect(370, 20, 171, 181))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_25 = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_4.addWidget(self.label_25)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("../../../../../../PycharmProjects/pythonProject/images/man.png"))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_4.addWidget(self.label_24)
        self.myTab.addTab(self.tab_2, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.myTab.addTab(self.tab_8, "")
        self.tabFinance = QtWidgets.QWidget()
        self.tabFinance.setObjectName("tabFinance")
        self.pushButton_22 = QtWidgets.QPushButton(self.tabFinance)
        self.pushButton_22.setGeometry(QtCore.QRect(460, 130, 131, 91))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_26 = QtWidgets.QPushButton(self.tabFinance)
        self.pushButton_26.setGeometry(QtCore.QRect(660, 130, 131, 91))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_20 = QtWidgets.QPushButton(self.tabFinance)
        self.pushButton_20.setGeometry(QtCore.QRect(230, 130, 131, 91))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_23 = QtWidgets.QPushButton(self.tabFinance)
        self.pushButton_23.setGeometry(QtCore.QRect(440, 460, 131, 91))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_27 = QtWidgets.QPushButton(self.tabFinance)
        self.pushButton_27.setGeometry(QtCore.QRect(650, 460, 131, 91))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_24 = QtWidgets.QPushButton(self.tabFinance)
        self.pushButton_24.setGeometry(QtCore.QRect(220, 460, 131, 91))
        self.pushButton_24.setObjectName("pushButton_24")
        self.myTab.addTab(self.tabFinance, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(120, 270, 191, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 270, 191, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 270, 191, 121))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.myTab.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.myTab)

        self.retranslateUi(Dialog)
        self.myTab.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HR Main Page"))
        self.label_34.setText(_translate("Dialog", "Name"))
        self.label_35.setText(_translate("Dialog", "Surname"))
        self.label_36.setText(_translate("Dialog", "Tel"))
        self.lblNameHome.setText(_translate("Dialog", "Mohamed "))
        self.lblSurnameHome.setText(_translate("Dialog", "Traore"))
        self.lblTelHome.setText(_translate("Dialog", "+905466216494"))
        self.label_40.setText(_translate("Dialog", "Email"))
        self.lblEmailHome.setText(_translate("Dialog", "traore.mohamed@std.izu.edu.tr"))
        self.btnFullProfileHome.setText(_translate("Dialog", "Full Profile"))
        self.btnUpdateProfileHome.setText(_translate("Dialog", "Update Profile"))
        self.label_32.setText(_translate("Dialog", "My Time Table"))
        self.btnAddHome.setText(_translate("Dialog", "Add"))
        self.btnDeleteHome.setText(_translate("Dialog", "Delete"))
        self.btnDeleteAllHome.setText(_translate("Dialog", "Delete All"))
        self.myTab.setTabText(self.myTab.indexOf(self.tab), _translate("Dialog", "Home page"))
        self.label_8.setText(_translate("Dialog", "Position"))
        self.btnShowAllShowProfiles.setText(_translate("Dialog", "Show All"))
        self.btnSearchByIdShowProfiles.setText(_translate("Dialog", "Search by Id"))
        self.btnSearchByNameShowProfiles.setText(_translate("Dialog", "Search by Name"))
        self.btnNewShowProfiles.setText(_translate("Dialog", "New"))
        self.btnUpdateShowProfiles.setText(_translate("Dialog", "Update"))
        self.btnDeleteShowProfiles.setText(_translate("Dialog", "Delete"))
        self.lblAddressShowProfiles.setText(_translate("Dialog", "Address"))
        self.lblPhoneShowProfiles.setText(_translate("Dialog", "Phone"))
        self.lblNameShowProfiles.setText(_translate("Dialog", "Name"))
        self.label_11.setText(_translate("Dialog", "Name"))
        self.label_13.setText(_translate("Dialog", "Phone"))
        self.label_14.setText(_translate("Dialog", "Email"))
        self.lblSurnameShowProfiles.setText(_translate("Dialog", "Name"))
        self.label_19.setText(_translate("Dialog", "Address"))
        self.label_12.setText(_translate("Dialog", "Surname"))
        self.lblEmailShowProfiles.setText(_translate("Dialog", "Phone"))
        self.label_22.setText(_translate("Dialog", "Identity"))
        self.lblIdentityShowProfiles.setText(_translate("Dialog", "Identity"))
        self.label_9.setText(_translate("Dialog", "Personel"))
        self.myTab.setTabText(self.myTab.indexOf(self.tab_7), _translate("Dialog", "Show Profiles"))
        self.label.setText(_translate("Dialog", "Add Personel"))
        self.label_3.setText(_translate("Dialog", "Identity"))
        self.label_4.setText(_translate("Dialog", "Name"))
        self.label_5.setText(_translate("Dialog", "Surname"))
        self.lnIdAddPersonel.setPlaceholderText(_translate("Dialog", "ID"))
        self.lnNameAddPersonel.setPlaceholderText(_translate("Dialog", "Name"))
        self.lnSurnameAddPersonel.setPlaceholderText(_translate("Dialog", "Surname"))
        self.label_6.setText(_translate("Dialog", "Phone"))
        self.lnPhoneAddPersonel.setPlaceholderText(_translate("Dialog", "555-555-5555"))
        self.label_7.setText(_translate("Dialog", "Email"))
        self.lnEmailAddPersonel.setPlaceholderText(_translate("Dialog", "m@gmail.com"))
        self.lnSalaryAddPersonel.setPlaceholderText(_translate("Dialog", "1000"))
        self.label_10.setText(_translate("Dialog", "Salary"))
        self.label_15.setText(_translate("Dialog", "Gender"))
        self.btnBrowseAddPersonel.setText(_translate("Dialog", "Browse"))
        self.label_16.setText(_translate("Dialog", "Picture"))
        self.label_17.setText(_translate("Dialog", "Address"))
        self.btnAddAddPersonel.setText(_translate("Dialog", "Add"))
        self.label_18.setText(_translate("Dialog", "TL"))
        self.btnClearAllAddPersonel.setText(_translate("Dialog", "Clear All"))
        self.rdMaleAddPersonel.setText(_translate("Dialog", "Male"))
        self.rdFemaleAddPersonel.setText(_translate("Dialog", "Female"))
        self.myTab.setTabText(self.myTab.indexOf(self.tab_6), _translate("Dialog", "Add Personel"))
        self.lnIdDeletePersonel.setPlaceholderText(_translate("Dialog", "ID or Full Name"))
        self.btnDeleteDeletePersonel.setText(_translate("Dialog", "Delete"))
        self.cmbIdDeletePersonel.setItemText(0, _translate("Dialog", "ID"))
        self.cmbIdDeletePersonel.setItemText(1, _translate("Dialog", "Full Name"))
        self.myTab.setTabText(self.myTab.indexOf(self.tab_5), _translate("Dialog", "Delete Personel"))
        self.lnIdUpdatePersonel.setPlaceholderText(_translate("Dialog", "ID"))
        self.btnLoadUpdatePersonel.setText(_translate("Dialog", "Load"))
        self.label_26.setText(_translate("Dialog", "Name"))
        self.label_27.setText(_translate("Dialog", "Surname"))
        self.label_28.setText(_translate("Dialog", "Phone"))
        self.label_30.setText(_translate("Dialog", "Email"))
        self.label_29.setText(_translate("Dialog", "Picture"))
        self.btnBrowseUpdatePersonel.setText(_translate("Dialog", "Browse"))
        self.label_31.setText(_translate("Dialog", "Address"))
        self.btnSaveUpdatePersonel.setText(_translate("Dialog", "Save"))
        self.btnCancelUpdatePersonel.setText(_translate("Dialog", "Cancel"))
        self.label_25.setText(_translate("Dialog", "Personel"))
        self.myTab.setTabText(self.myTab.indexOf(self.tab_2), _translate("Dialog", "Update Personel"))
        self.myTab.setTabText(self.myTab.indexOf(self.tab_8), _translate("Dialog", "Application management system"))
        self.pushButton_22.setText(_translate("Dialog", "HR Retention "))
        self.pushButton_26.setText(_translate("Dialog", "HR Retention "))
        self.pushButton_20.setText(_translate("Dialog", "HR Retention "))
        self.pushButton_23.setText(_translate("Dialog", "HR Retention "))
        self.pushButton_27.setText(_translate("Dialog", "HR Retention "))
        self.pushButton_24.setText(_translate("Dialog", "HR Retention "))
        self.myTab.setTabText(self.myTab.indexOf(self.tabFinance), _translate("Dialog", "Human Analyzer"))
        self.pushButton.setText(_translate("Dialog", "Show Salaries"))
        self.pushButton_2.setText(_translate("Dialog", "Adjust Prims"))
        self.pushButton_3.setText(_translate("Dialog", "Feasibility"))
        self.myTab.setTabText(self.myTab.indexOf(self.tab_3), _translate("Dialog", "Financial Operations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
