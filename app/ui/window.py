# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(640, 442)
        self.gridLayout = QtWidgets.QGridLayout(Window)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=Window)
        self.label.setMinimumSize(QtCore.QSize(0, 15))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dirEdit = QtWidgets.QLineEdit(parent=Window)
        self.dirEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.dirEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.dirEdit.setReadOnly(True)
        self.dirEdit.setObjectName("dirEdit")
        self.gridLayout.addWidget(self.dirEdit, 1, 0, 1, 1)
        self.loadFilesButton = QtWidgets.QPushButton(parent=Window)
        self.loadFilesButton.setMinimumSize(QtCore.QSize(0, 30))
        self.loadFilesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.loadFilesButton.setObjectName("loadFilesButton")
        self.gridLayout.addWidget(self.loadFilesButton, 1, 1, 1, 2)
        self.splitter = QtWidgets.QSplitter(parent=Window)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(parent=self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.srcFileList = QtWidgets.QListWidget(parent=self.widget)
        self.srcFileList.setObjectName("srcFileList")
        self.verticalLayout_2.addWidget(self.srcFileList)
        self.widget1 = QtWidgets.QWidget(parent=self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.widget1)
        self.label_3.setStyleSheet("font: 700 9pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.dstFileList = QtWidgets.QListWidget(parent=self.widget1)
        self.dstFileList.setObjectName("dstFileList")
        self.verticalLayout.addWidget(self.dstFileList)
        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(parent=Window)
        self.label_4.setMinimumSize(QtCore.QSize(0, 15))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.prefixEdit = QtWidgets.QLineEdit(parent=Window)
        self.prefixEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.prefixEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.prefixEdit.setObjectName("prefixEdit")
        self.gridLayout.addWidget(self.prefixEdit, 4, 0, 1, 1)
        self.renameFilesButton = QtWidgets.QPushButton(parent=Window)
        self.renameFilesButton.setMinimumSize(QtCore.QSize(0, 30))
        self.renameFilesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.renameFilesButton.setObjectName("renameFilesButton")
        self.gridLayout.addWidget(self.renameFilesButton, 4, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(parent=Window)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 3)
        self.extensionLabel = QtWidgets.QLabel(parent=Window)
        self.extensionLabel.setObjectName("extensionLabel")
        self.gridLayout.addWidget(self.extensionLabel, 4, 1, 1, 1)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Form"))
        self.label.setText(_translate("Window", "Répertoire courant"))
        self.loadFilesButton.setText(_translate("Window", "Sélectionner des fichiers"))
        self.label_2.setText(_translate("Window", "Fichiers sélectionnés"))
        self.label_3.setText(_translate("Window", "Fichiers renommés"))
        self.label_4.setText(_translate("Window", "Préfixe :"))
        self.prefixEdit.setPlaceholderText(_translate("Window", "..."))
        self.renameFilesButton.setText(_translate("Window", "Renommer"))
        self.extensionLabel.setText(_translate("Window", "*.jpg"))
