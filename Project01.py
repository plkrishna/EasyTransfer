# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import shutil
import re
class Ui_Application_main(object):
    def setupUi(self, Application_main):
        Application_main.setObjectName("Application_main")
        Application_main.setWindowModality(QtCore.Qt.WindowModal)
        Application_main.resize(552, 263)
        Application_main.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.centralwidget = QtWidgets.QWidget(Application_main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.SaveDefaultsButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveDefaultsButton.setObjectName("SaveDefaultsButton")
        self.horizontalLayout.addWidget(self.SaveDefaultsButton)
        self.RunDefaultsButton = QtWidgets.QPushButton(self.centralwidget)
        self.RunDefaultsButton.setObjectName("RunDefaultsButton")
        self.horizontalLayout.addWidget(self.RunDefaultsButton)
        self.RunButton = QtWidgets.QPushButton(self.centralwidget)
        self.RunButton.setObjectName("RunButton")
        self.horizontalLayout.addWidget(self.RunButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.SourceDestinationLayout = QtWidgets.QVBoxLayout()
        self.SourceDestinationLayout.setObjectName("SourceDestinationLayout")
        self.SourcePathLayout_V = QtWidgets.QVBoxLayout()
        self.SourcePathLayout_V.setObjectName("SourcePathLayout_V")
        self.Source_folder_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(17)
        self.Source_folder_label.setFont(font)
        self.Source_folder_label.setObjectName("Source_folder_label")
        self.SourcePathLayout_V.addWidget(self.Source_folder_label)
        self.SourcePathLayout_H = QtWidgets.QHBoxLayout()
        self.SourcePathLayout_H.setObjectName("SourcePathLayout_H")
        self.SourcePathInput = QtWidgets.QLineEdit(self.centralwidget)
        self.SourcePathInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SourcePathInput.setReadOnly(True)
        self.SourcePathInput.setObjectName("SourcePathInput")
        self.SourcePathLayout_H.addWidget(self.SourcePathInput)
        self.SourcePathSelector = QtWidgets.QPushButton(self.centralwidget)
        self.SourcePathSelector.setObjectName("SourcePathSelector")
        self.SourcePathLayout_H.addWidget(self.SourcePathSelector)
        self.SourcePathLayout_V.addLayout(self.SourcePathLayout_H)
        self.SourceDestinationLayout.addLayout(self.SourcePathLayout_V)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.SourceDestinationLayout.addItem(spacerItem)
        self.DestinationPathLayout_V = QtWidgets.QVBoxLayout()
        self.DestinationPathLayout_V.setObjectName("DestinationPathLayout_V")
        self.DestinationPathLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(17)
        self.DestinationPathLabel.setFont(font)
        self.DestinationPathLabel.setObjectName("DestinationPathLabel")
        self.DestinationPathLayout_V.addWidget(self.DestinationPathLabel)
        self.DestinationPathLayout_H = QtWidgets.QHBoxLayout()
        self.DestinationPathLayout_H.setObjectName("DestinationPathLayout_H")
        self.DestinationPathInput = QtWidgets.QLineEdit(self.centralwidget)
        self.DestinationPathInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DestinationPathInput.setReadOnly(True)
        self.DestinationPathInput.setObjectName("DestinationPathInput")
        self.DestinationPathLayout_H.addWidget(self.DestinationPathInput)
        self.DestionationPathSelector = QtWidgets.QPushButton(self.centralwidget)
        self.DestionationPathSelector.setObjectName("DestionationPathSelector")
        self.DestinationPathLayout_H.addWidget(self.DestionationPathSelector)
        self.DestinationPathLayout_V.addLayout(self.DestinationPathLayout_H)
        self.SourceDestinationLayout.addLayout(self.DestinationPathLayout_V)
        self.gridLayout.addLayout(self.SourceDestinationLayout, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        Application_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Application_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 552, 22))
        self.menubar.setObjectName("menubar")
        Application_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Application_main)
        self.statusbar.setObjectName("statusbar")
        Application_main.setStatusBar(self.statusbar)

        self.retranslateUi(Application_main)
        QtCore.QMetaObject.connectSlotsByName(Application_main)
        self.DestionationPathSelector.clicked.connect(self.openDestinationFolderSelector)
        self.SourcePathSelector.clicked.connect(self.openSourceFolderSelector)
        self.CancelButton.clicked.connect(Application_main.close)
        self.SaveDefaultsButton.clicked.connect(self.saveDefaultsMethod)
        self.RunDefaultsButton.clicked.connect(self.runDefaultsMethod)
        self.RunButton.clicked.connect(self.runMethod)
        self.RunButton.setEnabled(False)
        self.SaveDefaultsButton.setEnabled(False)
    def saveDefaultsMethod(self):
        with open('EasyTransferDefaultSettings.txt','w+') as f:
            f.write(self.SourcePathInput.text())
            f.write('\n')
            f.write(self.DestinationPathInput.text())
        os.chmod('EasyTransferDefaultSettings.txt',0o644)
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText('Your default settings are saved successfully!!')
        msg.setWindowTitle('Notification')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
    def runDefaultsMethod(self):
        currentPath=os.getcwd()
        checkList=os.listdir(currentPath)
        if not 'EasyTransferDefaultSettings.txt' in checkList:
            msg=QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("You don't have any default settings")
            msg.setWindowTitle('Alert')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            with open('EasyTransferDefaultSettings.txt','r+') as f:
                source=f.readline()
                destination=f.readline()
                source=source[:-1]
            self.transferFiles(source,destination)
    def transferFiles(self,source,destination):
        entries=os.scandir(source)
        l=[]
        for entry in entries:
            l.append(entry.name)
        arr=[]
        for i in l:
            x=re.search("^[0-9]{4}[a-z A-Z ]+",i)
            if x:
                arr.append(i)
        months={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
        for i in arr:
            source_dummy=source
            destination_dummy=destination+'/'
            name=i.split('.')
            print(name)
            month=name[0][-7:-5:1]
            source_dummy+='/'+i
            destination_dummy=destination_dummy+i[0:4]+'/correspondence'+'/'+months[month]
            print(source_dummy)
            print(destination_dummy)
            if os.path.isdir(destination_dummy):    
                new_path=shutil.move(source_dummy,destination_dummy)
            else:
                os.mkdir(destination_dummy)
                new_path=shutil.move(source_dummy,destination_dummy)
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText('Your files have been transferred successfully!!')
        msg.setWindowTitle('Notification')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def runMethod(self):
        self.transferFiles(self.SourcePathInput.text(),self.DestinationPathInput.text())
    def openDestinationFolderSelector(self):
        self.dlg=QtWidgets.QFileDialog()
        self.dlg.setFileMode(QtWidgets.QFileDialog.Directory)
        self.DestinationFolderPath=''
        self.DestinationPathInput.setText('')
        if self.dlg.exec_():
            self.DestinationPathInput.setText(self.dlg.selectedFiles()[0])
            self.DestinationPathInput.setReadOnly(False)
        if self.DestinationPathInput.text()!='' and self.SourcePathInput.text()!='':
            self.RunButton.setEnabled(True)
            self.SaveDefaultsButton.setEnabled(True)
        else:
            self.RunButton.setEnabled(False)
            self.SaveDefaultsButton.setEnabled(False)
    def openSourceFolderSelector(self):
        self.dlg=QtWidgets.QFileDialog()
        self.dlg.setFileMode(QtWidgets.QFileDialog.Directory)
        self.SourcePathInput.setText('')
        self.SourceFolderPath=''
        if self.dlg.exec_():
            self.SourcePathInput.setText(self.dlg.selectedFiles()[0])
            self.SourcePathInput.setReadOnly(False)
        if self.DestinationPathInput.text()!='' and self.SourcePathInput.text()!='':
            self.RunButton.setEnabled(True)
            self.SaveDefaultsButton.setEnabled(True)
        else:
            self.RunButton.setEnabled(False)
            self.SaveDefaultsButton.setEnabled(False)

    def retranslateUi(self, Application_main):
        _translate = QtCore.QCoreApplication.translate
        Application_main.setWindowTitle(_translate("Application_main", "EasyTransfer"))
        self.CancelButton.setText(_translate("Application_main", "Cancel"))
        self.SaveDefaultsButton.setText(_translate("Application_main", "Save as Defaults"))
        self.RunDefaultsButton.setText(_translate("Application_main", "Run with defaults"))
        self.RunButton.setText(_translate("Application_main", "Run"))
        self.Source_folder_label.setText(_translate("Application_main", "Specify your Source Folder"))
        self.SourcePathSelector.setText(_translate("Application_main", "Browse"))
        self.DestinationPathLabel.setText(_translate("Application_main", "Specify your Destination Folder"))
        self.DestionationPathSelector.setText(_translate("Application_main", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Application_main = QtWidgets.QMainWindow()
    ui = Ui_Application_main()
    ui.setupUi(Application_main)
    Application_main.show()
    sys.exit(app.exec_())

