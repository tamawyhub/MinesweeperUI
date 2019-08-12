# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MinesweeperUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow,self).__init__()
        self.setObjectName("MainWindow")
        self.resize(1052, 827)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.gridViewTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridViewTab.sizePolicy().hasHeightForWidth())
        self.gridViewTab.setSizePolicy(sizePolicy)
        self.gridViewTab.setObjectName("gridViewTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gridViewTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.gridViewTab)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setEditTriggers(self.tableWidget.NoEditTriggers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setRowCount(19)
        self.tableWidget.setColumnCount(19)
        self.tableWidget.setObjectName("tableWidget")

        for i in range (0, 19):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        for i in range (0, 19):
            for j in range (0, 19):
                item = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(40)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.legendFormLayout = QtWidgets.QFormLayout()
        self.legendFormLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.legendFormLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.legendFormLayout.setHorizontalSpacing(6)
        self.legendFormLayout.setObjectName("legendFormLayout")
        self.redLabel = QtWidgets.QLabel(self.gridViewTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.redLabel.setFont(font)
        self.redLabel.setStyleSheet("QLabel { color : red; }")
        self.redLabel.setObjectName("redLabel")
        self.legendFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.redLabel)
        self.burriedMineLabel = QtWidgets.QLabel(self.gridViewTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.burriedMineLabel.sizePolicy().hasHeightForWidth())
        self.burriedMineLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.burriedMineLabel.setFont(font)
        self.burriedMineLabel.setStyleSheet("QLabel { color : red; }")
        self.burriedMineLabel.setObjectName("burriedMineLabel")
        self.legendFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.burriedMineLabel)
        self.blueLabel = QtWidgets.QLabel(self.gridViewTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.blueLabel.setFont(font)
        self.blueLabel.setStyleSheet("QLabel { color : blue; }")
        self.blueLabel.setObjectName("blueLabel")
        self.legendFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.blueLabel)
        self.surfaceMineLabel = QtWidgets.QLabel(self.gridViewTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.surfaceMineLabel.sizePolicy().hasHeightForWidth())
        self.surfaceMineLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.surfaceMineLabel.setFont(font)
        self.surfaceMineLabel.setStyleSheet("QLabel { color : blue; }")
        self.surfaceMineLabel.setObjectName("surfaceMineLabel")
        self.legendFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surfaceMineLabel)
        self.greenLabel = QtWidgets.QLabel(self.gridViewTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.greenLabel.setFont(font)
        self.greenLabel.setStyleSheet("QLabel { color : green; }")
        self.greenLabel.setObjectName("greenLabel")
        self.legendFormLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.greenLabel)
        self.clearLabel = QtWidgets.QLabel(self.gridViewTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearLabel.sizePolicy().hasHeightForWidth())
        self.clearLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.clearLabel.setFont(font)
        self.clearLabel.setStyleSheet("QLabel { color : green; }")
        self.clearLabel.setObjectName("clearLabel")
        self.legendFormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.clearLabel)
        self.yellowLabel = QtWidgets.QLabel(self.gridViewTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.yellowLabel.setFont(font)
        self.yellowLabel.setStyleSheet("QLabel { color : yellow; }")
        self.yellowLabel.setObjectName("yellowLabel")
        self.legendFormLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.yellowLabel)
        self.unscanedLabel = QtWidgets.QLabel(self.gridViewTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unscanedLabel.sizePolicy().hasHeightForWidth())
        self.unscanedLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.unscanedLabel.setFont(font)
        self.unscanedLabel.setStyleSheet("QLabel { color : yellow; }")
        self.unscanedLabel.setObjectName("unscanedLabel")
        self.legendFormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.unscanedLabel)
        self.purpleLabel = QtWidgets.QLabel(self.gridViewTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.purpleLabel.setFont(font)
        self.purpleLabel.setStyleSheet("QLabel { color : purple; }")
        self.purpleLabel.setObjectName("purpleLabel")
        self.legendFormLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.purpleLabel)
        self.currentLabel = QtWidgets.QLabel(self.gridViewTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentLabel.sizePolicy().hasHeightForWidth())
        self.currentLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.currentLabel.setFont(font)
        self.currentLabel.setStyleSheet("QLabel { color : purple; }")
        self.currentLabel.setObjectName("currentLabel")
        self.legendFormLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.currentLabel)
        self.verticalLayout.addLayout(self.legendFormLayout)
        self.compassWidget = CompassWidget()
        self.verticalLayout.addWidget(self.compassWidget)
        self.toolkitVerticalLayout = QtWidgets.QVBoxLayout()
        self.toolkitVerticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.toolkitVerticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.toolkitVerticalLayout.setObjectName("toolkitVerticalLayout")
        self.mappingMethodLabel = QtWidgets.QLabel(self.gridViewTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mappingMethodLabel.sizePolicy().hasHeightForWidth())
        self.mappingMethodLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mappingMethodLabel.setFont(font)
        self.mappingMethodLabel.setObjectName("mappingMethodLabel")
        self.toolkitVerticalLayout.addWidget(self.mappingMethodLabel)
        self.manualRadioButton = QtWidgets.QRadioButton(self.gridViewTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manualRadioButton.sizePolicy().hasHeightForWidth())
        self.manualRadioButton.setSizePolicy(sizePolicy)
        self.manualRadioButton.setObjectName("manualRadioButton")
        self.toolkitVerticalLayout.addWidget(self.manualRadioButton)
        self.automaticRadioButton = QtWidgets.QRadioButton(self.gridViewTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.automaticRadioButton.sizePolicy().hasHeightForWidth())
        self.automaticRadioButton.setSizePolicy(sizePolicy)
        self.automaticRadioButton.setObjectName("automaticRadioButton")
        self.toolkitVerticalLayout.addWidget(self.automaticRadioButton)
        self.disabledRadioButton = QtWidgets.QRadioButton(self.gridViewTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disabledRadioButton.sizePolicy().hasHeightForWidth())
        self.disabledRadioButton.setSizePolicy(sizePolicy)
        self.disabledRadioButton.setChecked(True)
        self.disabledRadioButton.setObjectName("disabledRadioButton")
        self.toolkitVerticalLayout.addWidget(self.disabledRadioButton)
        self.widget = QtWidgets.QWidget(self.gridViewTab)
        self.widget.setEnabled(False)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 100, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.redButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redButton.sizePolicy().hasHeightForWidth())
        self.redButton.setSizePolicy(sizePolicy)
        self.redButton.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 110, 110, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #ff0000;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.redButton.setText("")
        self.redButton.setObjectName("redButton")
        self.gridLayout.addWidget(self.redButton, 0, 0, 1, 1)
        self.yellowButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yellowButton.sizePolicy().hasHeightForWidth())
        self.yellowButton.setSizePolicy(sizePolicy)
        self.yellowButton.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 50, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #ffff00;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.yellowButton.setText("")
        self.yellowButton.setObjectName("yellowButton")
        self.gridLayout.addWidget(self.yellowButton, 1, 1, 1, 1)
        self.greenButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greenButton.sizePolicy().hasHeightForWidth())
        self.greenButton.setSizePolicy(sizePolicy)
        self.greenButton.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(0, 255, 0, 255), stop:1 rgba(110, 255, 110, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #00ff00;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.greenButton.setText("")
        self.greenButton.setObjectName("greenButton")
        self.gridLayout.addWidget(self.greenButton, 1, 0, 1, 1)
        self.blueButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blueButton.sizePolicy().hasHeightForWidth())
        self.blueButton.setSizePolicy(sizePolicy)
        self.blueButton.setStyleSheet("QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(0, 0, 255, 255), stop:1 rgba(110, 110, 255, 255))\n"
"}\n"
"QPushButton {\n"
"     background-color: #0000ff;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(170, 170, 127)\n"
"}")
        self.blueButton.setText("")
        self.blueButton.setObjectName("blueButton")
        self.gridLayout.addWidget(self.blueButton, 0, 1, 1, 1)
        self.toolkitVerticalLayout.addWidget(self.widget)
        self.verticalLayout.addLayout(self.toolkitVerticalLayout)
        self.resetAllButton = QtWidgets.QPushButton(self.gridViewTab)
        self.resetAllButton.setObjectName("resetAllButton")
        self.verticalLayout.addWidget(self.resetAllButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.gridViewTab, "")
        self.cameraTab = QtWidgets.QWidget()
        self.cameraTab.setObjectName("cameraTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.cameraTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cameraFrame = QtWidgets.QFrame(self.cameraTab)
        self.cameraFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cameraFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cameraFrame.setObjectName("cameraFrame")
        self.verticalLayout_4.addWidget(self.cameraFrame)
        self.startStopStreamingButton = QtWidgets.QPushButton(self.cameraTab)
        self.startStopStreamingButton.setObjectName("startStopStreamingButton")
        self.verticalLayout_4.addWidget(self.startStopStreamingButton)
        self.tabWidget.addTab(self.cameraTab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.prepActions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minesweeper Map UI"))
        for i in range (0, 19):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", chr(ord('A')+i)))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.redLabel.setText(_translate("MainWindow", "Red:"))
        self.burriedMineLabel.setText(_translate("MainWindow", "Burried Mine"))
        self.blueLabel.setText(_translate("MainWindow", "Blue:"))
        self.surfaceMineLabel.setText(_translate("MainWindow", "Surface Mine"))
        self.greenLabel.setText(_translate("MainWindow", "Green:"))
        self.clearLabel.setText(_translate("MainWindow", "Clear"))
        self.yellowLabel.setText(_translate("MainWindow", "Yellow:"))
        self.unscanedLabel.setText(_translate("MainWindow", "Unscaned"))
        self.purpleLabel.setText(_translate("MainWindow", "Purple:"))
        self.currentLabel.setText(_translate("MainWindow", "Current"))
        self.mappingMethodLabel.setText(_translate("MainWindow", "Mapping method:"))
        self.manualRadioButton.setText(_translate("MainWindow", "Manual"))
        self.automaticRadioButton.setText(_translate("MainWindow", "Automatic"))
        self.disabledRadioButton.setText(_translate("MainWindow", "Disapled"))
        self.resetAllButton.setText(_translate("MainWindow", "Reset All!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gridViewTab), _translate("MainWindow", "Grid View"))
        self.startStopStreamingButton.setText(_translate("MainWindow", "Start Streaming"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cameraTab), _translate("MainWindow", "Camera"))

    def prepActions(self):
        self.disabledRadioButton.clicked['bool'].connect(self.tableWidget.setDisabled)
        self.automaticRadioButton.clicked['bool'].connect(self.tableWidget.setEnabled)
        self.manualRadioButton.clicked['bool'].connect(self.tableWidget.setEnabled)
        self.disabledRadioButton.clicked['bool'].connect(self.widget.setDisabled)
        self.automaticRadioButton.clicked['bool'].connect(self.widget.setDisabled)
        self.manualRadioButton.clicked['bool'].connect(self.widget.setEnabled)
        self.redButton.clicked.connect(self.colorButtonClicked)
        self.blueButton.clicked.connect(self.colorButtonClicked)
        self.greenButton.clicked.connect(self.colorButtonClicked)
        self.yellowButton.clicked.connect(self.colorButtonClicked)
        self.resetAllButton.clicked.connect(self.resetAllButtonClicked)
        self.startStopStreamingButton.clicked.connect(self.startStopStreamingButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(self)

    def colorButtonClicked(self):
        sender = self.sender()
        items=self.tableWidget.selectedItems()
        for item in items:
            if (sender == self.redButton):
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
            elif sender == self.blueButton:
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
            elif sender == self.yellowButton:
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
            else:
                brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)

    def resetAllButtonClicked(self):
        for i in range (0, 19):
            for j in range (0, 19):
                item = QtWidgets.QTableWidgetItem()
                brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
                self.tableWidget.setItem(i, j, item)

    def startStopStreamingButtonClicked(self):
        if self.startStopStreamingButton.text() == "Start Streaming":
            self.startStopStreamingButton.setText("Stop Streaming")
            self.cameraFrame.setEnabled(True)
        else:
            self.startStopStreamingButton.setText("Start Streaming")
            self.cameraFrame.setEnabled(False)

class CompassWidget(QtWidgets.QWidget):
    angleChanged = QtCore.pyqtSignal(float)
    
    def __init__(self, parent = None):
    
        super(QtWidgets.QWidget, self).__init__(parent)
        
        self._angle = 0.0
        self._margins = 10
        self._pointText = {0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S",
                           225: "SW", 270: "W", 315: "NW"}
    
    def paintEvent(self, event):
    
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        painter.fillRect(event.rect(), self.palette().brush(QtGui.QPalette.Window))
        self.drawMarkings(painter)
        self.drawNeedle(painter)
        
        painter.end()
    
    def drawMarkings(self, painter):
    
        painter.save()
        painter.translate(self.width()/2, self.height()/2)
        scale = min((self.width() - self._margins)/120.0,
                    (self.height() - self._margins)/120.0)
        painter.scale(scale, scale)
        
        font = QtGui.QFont(self.font())
        font.setPixelSize(10)
        metrics = QtGui.QFontMetricsF(font)
        
        painter.setFont(font)
        painter.setPen(self.palette().color(QtGui.QPalette.Shadow))
        
        i = 0
        while i < 360:
        
            if i % 45 == 0:
                painter.drawLine(0, -40, 0, -50)
                painter.drawText(-metrics.width(self._pointText[i])/2.0, -52,
                                 self._pointText[i])
            else:
                painter.drawLine(0, -45, 0, -50)
            
            painter.rotate(15)
            i += 15
        
        painter.restore()
    
    def drawNeedle(self, painter):
    
        painter.save()
        painter.translate(self.width()/2, self.height()/2)
        painter.rotate(self._angle)
        scale = min((self.width() - self._margins)/120.0,
                    (self.height() - self._margins)/120.0)
        painter.scale(scale, scale)
        
        painter.setPen(QtGui.QPen(QtCore.Qt.NoPen))
        painter.setBrush(self.palette().brush(QtGui.QPalette.Shadow))
        
        painter.drawPolygon(
            QtGui.QPolygon([QtCore.QPoint(-10, 0), QtCore.QPoint(0, -45), QtCore.QPoint(10, 0),
                      QtCore.QPoint(0, 45), QtCore.QPoint(-10, 0)])
            )
        
        painter.setBrush(self.palette().brush(QtGui.QPalette.Highlight))
        
        painter.drawPolygon(
            QtGui.QPolygon([QtCore.QPoint(-5, -25), QtCore.QPoint(0, -45), QtCore.QPoint(5, -25),
                      QtCore.QPoint(0, -30), QtCore.QPoint(-5, -25)])
            )
        
        painter.restore()
    
    def sizeHint(self):
    
        return QtCore.QSize(150, 150)
    
    def angle(self):
        return self._angle
    
    @QtCore.pyqtSlot(float)
    def setAngle(self, angle):
    
        if angle != self._angle:
            self._angle = angle
            self.angleChanged.emit(angle)
            self.update()
    
    angle = QtCore.pyqtProperty(float, angle, setAngle)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
