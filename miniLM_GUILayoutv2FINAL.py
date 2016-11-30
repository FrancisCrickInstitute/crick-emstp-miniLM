# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'miniLM_GUI-Layout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph as pg

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
        MainWindow.setGeometry(10, 25, 1170, 710)
        MainWindow.setMinimumSize(QtCore.QSize(700, 350))
        MainWindow.setMaximumSize(QtCore.QSize(1170, 710))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
       
        self.quitPushButton = QtGui.QPushButton(self.centralwidget)
        self.quitPushButton.setGeometry(QtCore.QRect(1030, 660, 80, 25))
        self.quitPushButton.setObjectName(_fromUtf8("quitPushButton"))
        self.liveImageGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.liveImageGroupBox.setGeometry(QtCore.QRect(680, 20, 461, 190))
        self.liveImageGroupBox.setObjectName(_fromUtf8("liveImageGroupBox"))
        self.widget = QtGui.QWidget(self.liveImageGroupBox)
        self.widget.setGeometry(QtCore.QRect(15, 31, 431, 160))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.fileLocationTextBrowser = QtGui.QTextBrowser(self.widget)
        self.fileLocationTextBrowser.setObjectName(_fromUtf8("fileLocationTextBrowser"))
        self.gridLayout_3.addWidget(self.fileLocationTextBrowser, 2, 0, 1, 2)
        self.stopButton = QtGui.QPushButton(self.widget)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.gridLayout_3.addWidget(self.stopButton, 0, 1, 1, 1)
        self.liveButton = QtGui.QPushButton(self.widget)
        self.liveButton.setObjectName(_fromUtf8("liveButton"))
        self.liveButton.setCheckable(True)
        self.gridLayout_3.addWidget(self.liveButton, 0, 0, 1, 1)
        self.saveCheckBox = QtGui.QCheckBox(self.widget)
        self.saveCheckBox.setObjectName(_fromUtf8("saveCheckBox"))
        self.gridLayout_3.addWidget(self.saveCheckBox, 0, 2, 1, 1)
        self.dirSelectionToolButton = QtGui.QToolButton(self.widget)
        self.dirSelectionToolButton.setObjectName(_fromUtf8("dirSelectionToolButton"))
        self.gridLayout_3.addWidget(self.dirSelectionToolButton, 2, 2, 1, 1)
        self.fileLocationLabel = QtGui.QLabel(self.widget)
        self.fileLocationLabel.setObjectName(_fromUtf8("fileLocationLabel"))
        self.gridLayout_3.addWidget(self.fileLocationLabel, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.imageNumberLabel = QtGui.QLabel(self.widget)
        self.imageNumberLabel.setObjectName(_fromUtf8("imageNumberLabel"))
        self.horizontalLayout_3.addWidget(self.imageNumberLabel)
        
        self.ImageNumberCounter = QtGui.QLCDNumber(self.widget)
        self.ImageNumberCounter.setObjectName(_fromUtf8("ImageNumberCounter"))
        self.ImageNumberCounter.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 89, 242);    \n"
"    background-color: rgb(0, 0, 85);\n"
"}"))
        
        self.horizontalLayout_3.addWidget(self.ImageNumberCounter)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.singleImageGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.singleImageGroupBox.setGeometry(QtCore.QRect(680, 210, 220, 79))
        self.singleImageGroupBox.setObjectName(_fromUtf8("singleImageGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.singleImageGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.snapButton = QtGui.QPushButton(self.singleImageGroupBox)
        self.snapButton.setObjectName(_fromUtf8("snapButton"))
        self.horizontalLayout_2.addWidget(self.snapButton)
        self.saveButton = QtGui.QPushButton(self.singleImageGroupBox)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.acquisitionPropertiesGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.acquisitionPropertiesGroupBox.setGeometry(QtCore.QRect(940, 210, 201, 141))
        self.acquisitionPropertiesGroupBox.setObjectName(_fromUtf8("acquisitionPropertiesGroupBox"))
        self.externalTriggerCheckBox = QtGui.QCheckBox(self.acquisitionPropertiesGroupBox)
        self.externalTriggerCheckBox.setGeometry(QtCore.QRect(20, 110, 160, 18))
        self.externalTriggerCheckBox.setObjectName(_fromUtf8("externalTriggerCheckBox"))
        self.line = QtGui.QFrame(self.acquisitionPropertiesGroupBox)
        self.line.setGeometry(QtCore.QRect(10, 90, 180, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.expTimeSpinBox = QtGui.QSpinBox(self.acquisitionPropertiesGroupBox)
        self.expTimeSpinBox.setGeometry(QtCore.QRect(20, 60, 110, 24))
        self.expTimeSpinBox.setMaximum(10000)
        self.expTimeSpinBox.setObjectName(_fromUtf8("expTimeSpinBox"))
        self.expTimeLabel = QtGui.QLabel(self.acquisitionPropertiesGroupBox)
        self.expTimeLabel.setGeometry(QtCore.QRect(20, 40, 117, 16))
        self.expTimeLabel.setObjectName(_fromUtf8("expTimeLabel"))
        self.externalTriggerCheckBox.raise_()
        self.line.raise_()
        self.zoomGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.zoomGroupBox.setGeometry(QtCore.QRect(680, 290, 220, 71))
        self.zoomGroupBox.setObjectName(_fromUtf8("zoomGroupBox"))
        self.zoomOutPushButton = QtGui.QPushButton(self.zoomGroupBox)
        self.zoomOutPushButton.setGeometry(QtCore.QRect(110, 30, 89, 32))
        self.zoomOutPushButton.setObjectName(_fromUtf8("zoomOutPushButton"))
        self.zoomInPushButton = QtGui.QPushButton(self.zoomGroupBox)
        self.zoomInPushButton.setGeometry(QtCore.QRect(10, 30, 97, 32))
        self.zoomInPushButton.setObjectName(_fromUtf8("zoomInPushButton"))
        self.quitPushButton.raise_()
        self.liveImageGroupBox.raise_()
        self.singleImageGroupBox.raise_()
        self.zoomInPushButton.raise_()
        self.zoomOutPushButton.raise_()
        self.acquisitionPropertiesGroupBox.raise_()
        self.expTimeLabel.raise_()
        self.expTimeLabel.raise_()
        self.ImageNumberCounter.raise_()
        self.imageNumberLabel.raise_()
        self.zoomOutPushButton.raise_()
        self.zoomGroupBox.raise_()

# Using Label to display image unlike v1 which used GraphicsView
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 650, 650))
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)#
 #       self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)#
  #      self.scrollArea.setWidgetResizable(True)#
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
 #       self.scrollAreaWidgetContents = QtGui.QWidget()

 #       self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 718, 718))
 #       self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        
        self.imageDisplayLabel = QtGui.QLabel(self.centralwidget)
        self.imageDisplayLabel.setGeometry(QtCore.QRect(20, 20, 0, 0))
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        
        self.imageDisplayLabel.setScaledContents(True) # This scales contents of label to size of label
##        sizePolicy.setHorizontalStretch(0)
##        sizePolicy.setVerticalStretch(0)
##        sizePolicy.setHeightForWidth(self.imageDisplayLabel.sizePolicy().hasHeightForWidth())
 #       self.imageDisplayLabel.setSizePolicy(sizePolicy)

        self.imageDisplayLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.imageDisplayLabel.setMouseTracking(True)
        self.imageDisplayLabel.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.imageDisplayLabel.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.imageDisplayLabel.setFrameShape(QtGui.QFrame.Box)
        self.imageDisplayLabel.setFrameShadow(QtGui.QFrame.Raised)
        self.imageDisplayLabel.setLineWidth(2)
        self.imageDisplayLabel.setMidLineWidth(0)
        self.imageDisplayLabel.setText(_fromUtf8(""))
        self.imageDisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageDisplayLabel.setObjectName(_fromUtf8("imageDisplayLabel"))


 #       self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.imageDisplayLabel)


#   Image properties - Histogram
        self.imagePropertiesGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.imagePropertiesGroupBox.setGeometry(QtCore.QRect(680, 365, 461, 291))
        self.imagePropertiesGroupBox.setObjectName(_fromUtf8("imagePropertiesGroupBox"))
        self.resetPushButton = QtGui.QPushButton(self.imagePropertiesGroupBox)
        self.resetPushButton.setGeometry(QtCore.QRect(370, 190, 76, 32))
        self.resetPushButton.setObjectName(_fromUtf8("resetPushButton"))
        # Histogram
 #       pg.setConfigOption('background', 'w')
        self.Histogram = pg.PlotWidget(self.imagePropertiesGroupBox)
        self.Histogram.setGeometry(QtCore.QRect(25, 135, 330, 140))
        self.Histogram.setObjectName(_fromUtf8("Histogram"))
        self.Histogram.setXRange(0, 256, 0)
        self.Histogram.setMouseEnabled(x=False, y=False)
        self.Histogram.showAxis('right', True)
        self.Histogram.showAxis('top', True)

 #       self.Histogram.setScale(0.8)
 
 

        
        self.widget = QtGui.QWidget(self.imagePropertiesGroupBox)
        self.widget.setGeometry(QtCore.QRect(21, 34, 421, 92))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.minLabel = QtGui.QLabel(self.widget)
        self.minLabel.setObjectName(_fromUtf8("minLabel"))
        self.gridLayout.addWidget(self.minLabel, 0, 0, 1, 1)
        self.minHorizontalSlider = QtGui.QSlider(self.widget)
        self.minHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.minHorizontalSlider.setMinimum(0)
        self.minHorizontalSlider.setMaximum(255)
        self.minHorizontalSlider.setObjectName(_fromUtf8("minHorizontalSlider"))
        self.gridLayout.addWidget(self.minHorizontalSlider, 0, 1, 1, 1)
        self.maxLabel = QtGui.QLabel(self.widget)
        self.maxLabel.setObjectName(_fromUtf8("maxLabel"))
        self.gridLayout.addWidget(self.maxLabel, 1, 0, 1, 1)
        self.maxHorizontalSlider = QtGui.QSlider(self.widget)
        self.maxHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.maxHorizontalSlider.setMinimum(0)
        self.maxHorizontalSlider.setMaximum(255)
        self.maxHorizontalSlider.setSliderPosition(255)
        self.maxHorizontalSlider.setObjectName(_fromUtf8("maxHorizontalSlider"))
        self.gridLayout.addWidget(self.maxHorizontalSlider, 1, 1, 1, 1)
        self.brightnessLabel = QtGui.QLabel(self.widget)
        self.brightnessLabel.setObjectName(_fromUtf8("brightnessLabel"))
        self.gridLayout.addWidget(self.brightnessLabel, 2, 0, 1, 1)
        self.brightnessHorizontalSlider = QtGui.QSlider(self.widget)
        self.brightnessHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessHorizontalSlider.setMinimum(-127)
        self.brightnessHorizontalSlider.setMaximum(128)
        self.brightnessHorizontalSlider.setSliderPosition(0)
        self.brightnessHorizontalSlider.setObjectName(_fromUtf8("brightnessHorizontalSlider"))
        self.gridLayout.addWidget(self.brightnessHorizontalSlider, 2, 1, 1, 1)




########################################


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1289, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
 #       QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.dirSelectionToolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.dirSelectionToolButton.showMenu)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "miniLM GUI", None))
        self.quitPushButton.setText(_translate("MainWindow", "Quit", None))
        self.liveImageGroupBox.setTitle(_translate("MainWindow", "Live Imaging", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.liveButton.setText(_translate("MainWindow", "Live", None))
        self.saveCheckBox.setText(_translate("MainWindow", "Save?", None))
        self.dirSelectionToolButton.setText(_translate("MainWindow", "...", None))
        self.fileLocationLabel.setText(_translate("MainWindow", "Files saved to:", None))
        self.imageNumberLabel.setText(_translate("MainWindow", "Acq. Image #", None))
        self.singleImageGroupBox.setTitle(_translate("MainWindow", "Single image", None))
        self.snapButton.setText(_translate("MainWindow", "Snap Image", None))
        self.saveButton.setText(_translate("MainWindow", "Save", None))
        self.acquisitionPropertiesGroupBox.setTitle(_translate("MainWindow", "Acqusition properties", None))
        self.externalTriggerCheckBox.setText(_translate("MainWindow", "Wait for external trigger", None))
        self.expTimeLabel.setText(_translate("MainWindow", "Exposure Time (ms)", None))
        self.zoomGroupBox.setTitle(_translate("MainWindow", "Zoom", None))
        self.zoomOutPushButton.setText(_translate("MainWindow", "Zoom out", None))
        self.zoomInPushButton.setText(_translate("MainWindow", "Zoom in", None))
        self.imagePropertiesGroupBox.setTitle(_translate("MainWindow", "Image properties", None))
 #       self.Histogram.setText(_translate("MainWindow", "Histogram Place Holder", None))
        self.minLabel.setText(_translate("MainWindow", "Min", None))
        self.maxLabel.setText(_translate("MainWindow", "Max", None))
        self.resetPushButton.setText(_translate("MainWindow", "Reset", None))
        self.brightnessLabel.setText(_translate("MainWindow", "Brightness", None))



