# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(816, 512)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(816, 512))
        MainWindow.setMaximumSize(QtCore.QSize(816, 512))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frameX = QtGui.QFrame(self.centralwidget)
        self.frameX.setGeometry(QtCore.QRect(9, 9, 256, 444))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameX.sizePolicy().hasHeightForWidth())
        self.frameX.setSizePolicy(sizePolicy)
        self.frameX.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameX.setFrameShadow(QtGui.QFrame.Plain)
        self.frameX.setObjectName(_fromUtf8("frameX"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frameX)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelFFTx = QtGui.QLabel(self.frameX)
        self.labelFFTx.setObjectName(_fromUtf8("labelFFTx"))
        self.verticalLayout.addWidget(self.labelFFTx)
        self.grFFTx = PlotWidget(self.frameX)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grFFTx.sizePolicy().hasHeightForWidth())
        self.grFFTx.setSizePolicy(sizePolicy)
        self.grFFTx.setMinimumSize(QtCore.QSize(150, 200))
        self.grFFTx.setObjectName(_fromUtf8("grFFTx"))
        self.verticalLayout.addWidget(self.grFFTx)
        self.labelAx = QtGui.QLabel(self.frameX)
        self.labelAx.setObjectName(_fromUtf8("labelAx"))
        self.verticalLayout.addWidget(self.labelAx)
        self.grAccX = PlotWidget(self.frameX)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grAccX.sizePolicy().hasHeightForWidth())
        self.grAccX.setSizePolicy(sizePolicy)
        self.grAccX.setMinimumSize(QtCore.QSize(150, 200))
        self.grAccX.setSizeIncrement(QtCore.QSize(0, 0))
        self.grAccX.setObjectName(_fromUtf8("grAccX"))
        self.verticalLayout.addWidget(self.grAccX)
        self.frameY = QtGui.QFrame(self.centralwidget)
        self.frameY.setGeometry(QtCore.QRect(280, 10, 256, 444))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameY.sizePolicy().hasHeightForWidth())
        self.frameY.setSizePolicy(sizePolicy)
        self.frameY.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameY.setFrameShadow(QtGui.QFrame.Plain)
        self.frameY.setObjectName(_fromUtf8("frameY"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frameY)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelFFTy = QtGui.QLabel(self.frameY)
        self.labelFFTy.setObjectName(_fromUtf8("labelFFTy"))
        self.verticalLayout_2.addWidget(self.labelFFTy)
        self.grFFTy = PlotWidget(self.frameY)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grFFTy.sizePolicy().hasHeightForWidth())
        self.grFFTy.setSizePolicy(sizePolicy)
        self.grFFTy.setMinimumSize(QtCore.QSize(150, 200))
        self.grFFTy.setObjectName(_fromUtf8("grFFTy"))
        self.verticalLayout_2.addWidget(self.grFFTy)
        self.labelAy = QtGui.QLabel(self.frameY)
        self.labelAy.setObjectName(_fromUtf8("labelAy"))
        self.verticalLayout_2.addWidget(self.labelAy)
        self.grAccY = PlotWidget(self.frameY)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grAccY.sizePolicy().hasHeightForWidth())
        self.grAccY.setSizePolicy(sizePolicy)
        self.grAccY.setMinimumSize(QtCore.QSize(150, 200))
        self.grAccY.setSizeIncrement(QtCore.QSize(0, 0))
        self.grAccY.setObjectName(_fromUtf8("grAccY"))
        self.verticalLayout_2.addWidget(self.grAccY)
        self.frameZ = QtGui.QFrame(self.centralwidget)
        self.frameZ.setGeometry(QtCore.QRect(550, 10, 256, 444))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameZ.sizePolicy().hasHeightForWidth())
        self.frameZ.setSizePolicy(sizePolicy)
        self.frameZ.setMinimumSize(QtCore.QSize(256, 0))
        self.frameZ.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameZ.setFrameShadow(QtGui.QFrame.Plain)
        self.frameZ.setObjectName(_fromUtf8("frameZ"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frameZ)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelFFTz = QtGui.QLabel(self.frameZ)
        self.labelFFTz.setObjectName(_fromUtf8("labelFFTz"))
        self.verticalLayout_3.addWidget(self.labelFFTz)
        self.grFFTz = PlotWidget(self.frameZ)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grFFTz.sizePolicy().hasHeightForWidth())
        self.grFFTz.setSizePolicy(sizePolicy)
        self.grFFTz.setMinimumSize(QtCore.QSize(150, 200))
        self.grFFTz.setObjectName(_fromUtf8("grFFTz"))
        self.verticalLayout_3.addWidget(self.grFFTz)
        self.labelAz = QtGui.QLabel(self.frameZ)
        self.labelAz.setObjectName(_fromUtf8("labelAz"))
        self.verticalLayout_3.addWidget(self.labelAz)
        self.grAccZ = PlotWidget(self.frameZ)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grAccZ.sizePolicy().hasHeightForWidth())
        self.grAccZ.setSizePolicy(sizePolicy)
        self.grAccZ.setMinimumSize(QtCore.QSize(150, 200))
        self.grAccZ.setSizeIncrement(QtCore.QSize(0, 0))
        self.grAccZ.setObjectName(_fromUtf8("grAccZ"))
        self.verticalLayout_3.addWidget(self.grAccZ)
        self.btnStartStream = QtGui.QPushButton(self.centralwidget)
        self.btnStartStream.setGeometry(QtCore.QRect(480, 460, 75, 23))
        self.btnStartStream.setToolTip(_fromUtf8(""))
        self.btnStartStream.setCheckable(False)
        self.btnStartStream.setObjectName(_fromUtf8("btnStartStream"))
        self.btnStartRecord = QtGui.QPushButton(self.centralwidget)
        self.btnStartRecord.setGeometry(QtCore.QRect(650, 460, 75, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStartRecord.sizePolicy().hasHeightForWidth())
        self.btnStartRecord.setSizePolicy(sizePolicy)
        self.btnStartRecord.setObjectName(_fromUtf8("btnStartRecord"))
        self.btnStopStream = QtGui.QPushButton(self.centralwidget)
        self.btnStopStream.setGeometry(QtCore.QRect(560, 460, 75, 23))
        self.btnStopStream.setToolTip(_fromUtf8(""))
        self.btnStopStream.setCheckable(False)
        self.btnStopStream.setObjectName(_fromUtf8("btnStopStream"))
        self.btnStopRecord = QtGui.QPushButton(self.centralwidget)
        self.btnStopRecord.setGeometry(QtCore.QRect(730, 460, 75, 23))
        self.btnStopRecord.setObjectName(_fromUtf8("btnStopRecord"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 460, 69, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.btnOpenPort = QtGui.QPushButton(self.centralwidget)
        self.btnOpenPort.setGeometry(QtCore.QRect(170, 460, 75, 23))
        self.btnOpenPort.setCheckable(True)
        self.btnOpenPort.setChecked(False)
        self.btnOpenPort.setObjectName(_fromUtf8("btnOpenPort"))
        self.btnRefreshList = QtGui.QPushButton(self.centralwidget)
        self.btnRefreshList.setGeometry(QtCore.QRect(90, 460, 75, 23))
        self.btnRefreshList.setObjectName(_fromUtf8("btnRefreshList"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 816, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuDatei = QtGui.QMenu(self.menuBar)
        self.menuDatei.setObjectName(_fromUtf8("menuDatei"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionData_Folder = QtGui.QAction(MainWindow)
        self.actionData_Folder.setObjectName(_fromUtf8("actionData_Folder"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setMenuRole(QtGui.QAction.QuitRole)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionCom_Port = QtGui.QAction(MainWindow)
        self.actionCom_Port.setMenuRole(QtGui.QAction.PreferencesRole)
        self.actionCom_Port.setSoftKeyRole(QtGui.QAction.NoSoftKey)
        self.actionCom_Port.setObjectName(_fromUtf8("actionCom_Port"))
        self.menuDatei.addAction(self.actionData_Folder)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionClose)
        self.menuBar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "WindLab Dynamic Experiment", None))
        self.labelFFTx.setText(_translate("MainWindow", "FFT x", None))
        self.labelAx.setText(_translate("MainWindow", "Acc x", None))
        self.labelFFTy.setText(_translate("MainWindow", "FFT y", None))
        self.labelAy.setText(_translate("MainWindow", "Acc y", None))
        self.labelFFTz.setText(_translate("MainWindow", "FFT z", None))
        self.labelAz.setText(_translate("MainWindow", "Acc z", None))
        self.btnStartStream.setText(_translate("MainWindow", "Start Stream", None))
        self.btnStartRecord.setText(_translate("MainWindow", "Start Record", None))
        self.btnStopStream.setText(_translate("MainWindow", "Stop Stream", None))
        self.btnStopRecord.setText(_translate("MainWindow", "Stop Record", None))
        self.comboBox.setToolTip(_translate("MainWindow", "Select Com Port", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "testItem1", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "testItem2", None))
        self.btnOpenPort.setText(_translate("MainWindow", "Open Port", None))
        self.btnRefreshList.setText(_translate("MainWindow", "Refresh List", None))
        self.menuDatei.setTitle(_translate("MainWindow", "Data", None))
        self.actionData_Folder.setText(_translate("MainWindow", "Select Data Folder", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionCom_Port.setText(_translate("MainWindow", "Com Port", None))

from pyqtgraph import PlotWidget
