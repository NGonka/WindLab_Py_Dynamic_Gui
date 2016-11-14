from PyQt4 import QtGui,QtCore
import sys
import ui_main2 as ui_main
import numpy as np
import pylab
import time
import pyqtgraph
import DataHandling


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

class Dynamic_Gui(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background','w')
        super(Dynamic_Gui, self).__init__(parent)
        self.setupUi(self)
        self.grFFTx.plotItem.showGrid(True,True, 0.7)
        self.grFFTy.plotItem.showGrid(True,True, 0.7)
        self.grFFTz.plotItem.showGrid(True,True, 0.7)
        self.grAccX.plotItem.showGrid(True,True, 0.7)
        self.grAccY.plotItem.showGrid(True,True, 0.7)
        self.grAccZ.plotItem.showGrid(True,True, 0.7)
        self.maxFFTx=0
        self.maxFFTy=0
        self.maxFFTz=0
        self.maxAccX=0
        self.maxAccY=0
        self.maxAccZ=0
        self.textEdit= "Hello World!"
        
        #read available com ports
        self.data= DataHandling.DataHandling()
        self.comboBox.clear()
        self.comboBox.addItem("Select...")
        for p in self.data.portList(): self.comboBox.addItem(str(p))
        self.comboBox.currentIndexChanged.connect(self._connectComPort)
        # self.comboBox.highlighted.connect(self._connectComPort)
        
        #connect the buttons
        self.btnOpenPort.clicked.connect(self._btnOpenPort)
        self.btnStartStream.clicked.connect(self._btnStartStream)
        self.btnStopStream.clicked.connect(self._btnStopStream)
        # self.actionClose.triggered.connect(QtGui.qApp.quit)
        self.actionData_Folder.triggered.connect(self._actionFolderSave)
        
        
    
    def _connectComPort(self,idx):
        if idx==0:
            print("idx = 0")
            return
        
        try:
            print("Current selcted Com Port: %s"%str(self.data.portList()[idx-1]))
            self.data.setPort(str(self.data.portList()[idx-1]))
            
        except:
            print("No Ports available")
            self.comboBox.setToolTip(_translate("MainWindow", "No Ports available", None))
    
    def _btnOpenPort(self,checked):
        print("_btnOpenPort test: %s"%checked)  
        if checked:
            try:
                if not self.data.openCom():
                    self.btnOpenPort.setChecked(False)
                else:
                    self.btnOpenPort.setText(_translate("MainWindow", "Close Port", None))
            except:
                print("_btnOpenPort Cannot connect to com Port: %s"%self.data.port)
                
        else:
            if not self.data.closeCom():
                
                print("_btnOpenPort Cannot close serial connection")
            else:
                self.btnOpenPort.setText(_translate("MainWindow", "Open Port", None))
    
    def update(self):
        QtCore.QTimer.singleShot(1, self.update) # QUICKLY repeat
        
    def _btnStartStream(self):
        self.data.start_data_stream()
        
    def _btnStopStream(self):
        self.data.stop_data_stream()
        
    # def _actionClose(self):
        # QtGui.QApplication.exit(0)
        
    def _actionFolderSave(self):
        name= str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        print ("Name: "+name)
        # file = open(name, 'w')
        # text = self.textEdit
        # file.write(text)
        # file.close()
    
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = Dynamic_Gui()
    form.show()
    form.update() #start with something
    app.exec_()
    print("DONE")
    
    
    

