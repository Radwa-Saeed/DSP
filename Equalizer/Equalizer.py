# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound 
import os
from PyQt5.QtWidgets import QSlider
from PyQt5 import QtCore, QtGui, QtWidgets ,QtPrintSupport
import pandas as pd
import numpy as np
import wavio
import sys
from pyqtgraph import PlotWidget ,PlotItem
import pathlib
import pyqtgraph as pg 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.fftpack import rfft
import scipy.fftpack as fftpk
import scipy
from scipy.io import wavfile
import math
import librosa
# from PyQt5 import QtCore, QtMultimedia

class Ui_MainWindow(QtGui.QMainWindow):
    count=-1
    equalizers=[]
    signals = []
    timer = []
    data = []
    h=[]
    speed=[]
    xmin=[0,0,0]
    xmax=[0,0,0]
    scrollrate=[]
    n = []
    nn = []
    data_line = []
    r = [1200,1200,1200]
    z = [1,1,1]
    spectrogram = []
    checkBox = []
    counter = -1
    fs=[]
    gain=[]

   
    Current = {'min':0, 'max':5}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 878)
        mW = QtGui.QIcon("Mw.png")
        MainWindow.setWindowIcon(mW)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        for i in range(0,12):
            self.equalizers.append(QtWidgets.QSlider(self.centralwidget))

            if i ==0:
                self.equalizers[i].setGeometry(QtCore.QRect(81, 340, 22, 221))
                self.equalizers[i].setObjectName("eq1")
                self.equalizers[i].setValue(1)

            elif i ==1:
                self.equalizers[i].setGeometry(QtCore.QRect(170, 340, 22, 221))
                self.equalizers[i].setObjectName("eq2")
                self.equalizers[i].setValue(1)

            elif i ==2:
                self.equalizers[i].setGeometry(QtCore.QRect(259, 340, 22, 221))
                self.equalizers[i].setObjectName("eq3")
                self.equalizers[i].setValue(1)

            elif i ==3:
                self.equalizers[i].setGeometry(QtCore.QRect(348, 340, 22, 221))
                self.equalizers[i].setObjectName("eq4")
                self.equalizers[i].setValue(1)

            elif i ==4:
                self.equalizers[i].setGeometry(QtCore.QRect(437, 340, 22, 221))
                self.equalizers[i].setObjectName("eq5")
                self.equalizers[i].setValue(1)
            elif i ==5:
                self.equalizers[i].setGeometry(QtCore.QRect(526, 340, 22, 221))
                self.equalizers[i].setObjectName("eq6")
                self.equalizers[i].setValue(1)

            elif i ==6:
                self.equalizers[i].setGeometry(QtCore.QRect(615, 340, 22, 221))
                self.equalizers[i].setObjectName("eq7")
                self.equalizers[i].setValue(1)
            elif i ==7:
                self.equalizers[i].setGeometry(QtCore.QRect(700, 340, 22, 221))
                self.equalizers[i].setObjectName("eq8")
                self.equalizers[i].setValue(1)
            elif i ==8:
                self.equalizers[i].setGeometry(QtCore.QRect(793, 340, 22, 221))
                self.equalizers[i].setObjectName("eq9")
                self.equalizers[i].setValue(1)
            elif i==9 :
                self.equalizers[i].setGeometry(QtCore.QRect(882, 340, 22, 221))
                self.equalizers[i].setObjectName("eq10")
                self.equalizers[i].setValue(1)
            elif i==10:
                self.equalizers[i].setGeometry(QtCore.QRect(960, 600, 22, 221))
                self.equalizers[i].setObjectName("Spec-min")
                self.equalizers[i].setValue(0)
                # self.equalizers[i].setMinimum(1)
                

            else:
                self.equalizers[i].setGeometry(QtCore.QRect(990, 600, 22, 221))
                self.equalizers[i].setObjectName("Spec-max")
                self.equalizers[i].setValue(5)

            self.equalizers[i].setTabletTracking(False)
            self.equalizers[i].setMaximum(5)
            self.equalizers[i].setOrientation(QtCore.Qt.Vertical)
            self.equalizers[i].setTickPosition(QSlider.TicksRight)
            self.equalizers[i].setTickInterval(1)
            self.equalizers[i].hide()


            
        for i in range(0,3):

            self.signals.append( PlotWidget(self.centralwidget))
        
            self.spectrogram.append( QtWidgets.QLabel(self.centralwidget))

            self.checkBox.append(QtWidgets.QCheckBox(self.centralwidget))
            if i == 0:
                self.signals[i].setGeometry(QtCore.QRect(20, 90, 461, 192))
                self.signals[i].setObjectName("signal_1")

                self.spectrogram[i].setGeometry(QtCore.QRect(490, 90, 471, 192))
                self.spectrogram[i].setObjectName("spectro_1")

                self.checkBox[i].setGeometry(QtCore.QRect(20, 50, 68, 20))
                self.checkBox[i].setObjectName("check_1")

            elif i == 1:
                self.signals[i].setGeometry(QtCore.QRect(20, 340, 461, 192))
                self.signals[i].setObjectName("signal_2")

                self.spectrogram[i].setGeometry(QtCore.QRect(490, 340, 471, 192))
                self.spectrogram[i].setObjectName("spectro_2")

                self.checkBox[i].setGeometry(QtCore.QRect(20, 300, 68, 20))
                self.checkBox[i].setObjectName("check_2")

            else:
                self.signals[i].setGeometry(QtCore.QRect(20, 600, 461, 192))
                self.signals[i].setObjectName("signal_3")

                self.spectrogram[i].setGeometry(QtCore.QRect(490, 600, 471, 192))
                self.spectrogram[i].setObjectName("spectro_3")

                self.checkBox[i].setGeometry(QtCore.QRect(20, 560, 68, 20))
                self.checkBox[i].setObjectName("check_3")


            self.signals[i].setStyleSheet("background-color:rgb(0, 0, 0);")
            # self.signals[i].setRubberBandSelectionMode(QtCore.Qt.IntersectsItemBoundingRect)
            self.signals[i].plotItem.showGrid(x=True, y=True )
            self.signals[i].plotItem.setMenuEnabled(False)

            self.checkBox[i].setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")

            self.spectrogram[i].setScaledContents(True)



        
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(0, 1, 35, 35))
        self.open.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open.setIcon(icon3)
        self.open.setObjectName("open")

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(35, 1, 35, 35))
        self.save.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon2)
        self.save.setObjectName("save")
        
        
        self.Zoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.Zoom_in.setGeometry(QtCore.QRect(70, 1, 35, 35))
        self.Zoom_in.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Zoom_in.setIcon(icon)
        self.Zoom_in.setObjectName("Zoom_in")

        self.zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out.setGeometry(QtCore.QRect(105, 1, 35, 35))
        self.zoom_out.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out.setIcon(icon1)
        self.zoom_out.setObjectName("zoom_out")


        self.down = QtWidgets.QPushButton(self.centralwidget)
        self.down.setGeometry(QtCore.QRect(140, 1, 35, 35))
        self.down.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("img/down.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.down.setIcon(icon21)
        self.down.setObjectName("down")




        self.left = QtWidgets.QPushButton(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(175, 1, 35, 35))
        self.left.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left.setIcon(icon7)
        self.left.setObjectName("left")

        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(210, 1, 35, 35))
        self.play.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon5)
        self.play.setObjectName("play")

        
        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(245, 1, 35, 35))
        self.right.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right.setIcon(icon6)
        self.right.setObjectName("right")


        self.up = QtWidgets.QPushButton(self.centralwidget)
        self.up.setGeometry(QtCore.QRect(280, 1, 35, 35))
        self.up.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("img/up.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up.setIcon(icon20)
        self.up.setObjectName("up")


        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(315, 1, 35, 35))
        self.pause.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause.setIcon(icon4)
        self.pause.setObjectName("pause")

        
        self.spec = QtWidgets.QPushButton(self.centralwidget)
        self.spec.setGeometry(QtCore.QRect(350, 1, 35, 35))
        self.spec.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("img/spec3.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.spec.setIcon(icon20)
        self.spec.setObjectName("spec")


        self.sound = QtWidgets.QPushButton(self.centralwidget)
        self.sound.setGeometry(QtCore.QRect(385, 1, 35, 35))
        self.sound.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("img/sound.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.sound.setIcon(icon22)
        self.sound.setObjectName("sound")


        self.wav = QtWidgets.QPushButton(self.centralwidget)
        self.wav.setGeometry(QtCore.QRect(420, 1, 35, 35))
        self.wav.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("img/wav.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.wav.setIcon(icon23)
        self.wav.setObjectName("wav")

        self.new = QtWidgets.QPushButton(self.centralwidget)
        self.new.setGeometry(QtCore.QRect(455, 1, 35, 35))
        self.new.setText("")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("img/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.new.setIcon(icon24)
        self.new.setObjectName("new")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(810, 285, 151, 31))
        self.comboBox.setEditable(True)
        self.comboBox.setIconSize(QtCore.QSize(30, 30))
        self.comboBox.setObjectName("comboBox")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon9, "")
        self.comboBox.addItem(icon9, "")
        self.comboBox.addItem(icon9, "")
        self.comboBox.addItem(icon9, "")
        self.comboBox.addItem(icon9, "")
        self.comboBox.hide()
       
        self.Zoom_in.raise_()
        self.equalizers[0].raise_()
        self.equalizers[1].raise_()
        self.equalizers[2].raise_()
        self.equalizers[3].raise_()
        self.equalizers[4].raise_()
        self.equalizers[5].raise_()
        self.equalizers[6].raise_()
        self.equalizers[7].raise_()
        self.equalizers[8].raise_()
        self.equalizers[9].raise_()
        self.equalizers[10].raise_()
        self.equalizers[11].raise_()
        self.signals[0].raise_()
        self.checkBox[1].raise_()
        self.spectrogram[1].raise_()
        self.spectrogram[2].raise_()
        self.checkBox[2].raise_()
        self.spectrogram[0].raise_()
        self.signals[1].raise_()
        self.signals[2].raise_()
        self.checkBox[0].raise_()
        self.zoom_out.raise_()
        self.save.raise_()
        self.open.raise_()
        self.pause.raise_()
        self.play.raise_()
        self.right.raise_()
        self.left.raise_()
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSignal_tools = QtWidgets.QMenu(self.menubar)
        self.menuSignal_tools.setObjectName("menuSignal_tools")
        self.menuPlay_navigate = QtWidgets.QMenu(self.menubar)
        self.menuPlay_navigate.setObjectName("menuPlay_navigate")
        MainWindow.setMenuBar(self.menubar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon9)
        self.actionOpen.setObjectName("actionOpen")
        
        self.actionzoom_in = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("zoom-in_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionzoom_in.setIcon(icon10)
        self.actionzoom_in.setObjectName("actionzoom_in")
        self.actionzoom_out = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionzoom_out.setIcon(icon11)
        self.actionzoom_out.setObjectName("actionzoom_out")
        self.actionSpectrogram = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpectrogram.setIcon(icon12)
        self.actionSpectrogram.setObjectName("actionSpectrogram")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlay.setIcon(icon13)
        self.actionPlay.setObjectName("actionPlay")
        self.actionPause = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("pause-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPause.setIcon(icon14)
        self.actionPause.setObjectName("actionPause")
        
        self.actionBackward = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("backward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBackward.setIcon(icon16)
        self.actionBackward.setObjectName("actionBackward")
        self.actionForward = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionForward.setIcon(icon17)
        self.actionForward.setObjectName("actionForward")
        self.actionSave_as_pdf = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("pdf-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as_pdf.setIcon(icon18)
        self.actionSave_as_pdf.setObjectName("actionSave_as_pdf")

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_as_pdf)
        self.menuEdit.addAction(self.actionzoom_in)
        self.menuEdit.addAction(self.actionzoom_out)
        self.menuSignal_tools.addAction(self.actionSpectrogram)
        self.menuPlay_navigate.addAction(self.actionPlay)
        self.menuPlay_navigate.addAction(self.actionPause)
        self.menuPlay_navigate.addSeparator()
        self.menuPlay_navigate.addAction(self.actionBackward)
        self.menuPlay_navigate.addAction(self.actionForward)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuPlay_navigate.menuAction())
        self.menubar.addAction(self.menuSignal_tools.menuAction())
        self.signals[0].hide()
        self.checkBox[0].hide()
        self.spectrogram[0].hide()
        self.signals[1].hide()
        self.checkBox[1].hide()
        self.spectrogram[1].hide() 
        self.signals[2].hide()
        self.checkBox[2].hide()
        self.spectrogram[2].hide()
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionOpen.triggered.connect(lambda:self.opensignal())

        self.actionzoom_in.triggered.connect(lambda:self.zoomin())
        self.actionzoom_out.triggered.connect(lambda:self.zoomout())
        self.actionSave_as_pdf.triggered.connect(lambda:self.savepdf())
        self.actionBackward.triggered.connect(lambda:self.scrlleft())
        self.actionForward.triggered.connect(lambda:self.scrlright())
        self.actionSpectrogram.triggered.connect(lambda:self.spectro())
        self.actionPlay.triggered.connect(lambda:self.playy())
        self.actionPause.triggered.connect(lambda:self.pausee())
    
        self.Zoom_in.clicked.connect(lambda:self.zoomin())
        self.zoom_out.clicked.connect(lambda:self.zoomout())
        self.left.clicked.connect(lambda:self.scrlleft())
        self.right.clicked.connect(lambda:self.scrlright())
        self.pause.clicked.connect(lambda:self.pausee())
        self.play.clicked.connect(lambda:self.playy())
        self.open.clicked.connect(lambda:self.opensignal())
        self.save.clicked.connect(lambda:self.savepdf())
        self.spec.clicked.connect(lambda:self.spectro())
        self.up.clicked.connect(lambda:self.SpeedUp())
        self.down.clicked.connect(lambda:self.SpeedDown())
        self.sound.clicked.connect(lambda:self.sounds())
        self.wav.clicked.connect(lambda:self.wave())
        self.new.clicked.connect(lambda:self.new_window())



        self.equalizers[0].valueChanged.connect(lambda:self.update(0))
        self.equalizers[1].valueChanged.connect(lambda:self.update(1))
        self.equalizers[2].valueChanged.connect(lambda:self.update(2))
        self.equalizers[3].valueChanged.connect(lambda:self.update(3))
        self.equalizers[4].valueChanged.connect(lambda:self.update(4))
        self.equalizers[5].valueChanged.connect(lambda:self.update(5))
        self.equalizers[6].valueChanged.connect(lambda:self.update(6))
        self.equalizers[7].valueChanged.connect(lambda:self.update(7))
        self.equalizers[8].valueChanged.connect(lambda:self.update(8))
        self.equalizers[9].valueChanged.connect(lambda:self.update(9))
        self.equalizers[10].valueChanged.connect(lambda:self.SpectroSliders(self.equalizers[10], 'min'))
        self.equalizers[11].valueChanged.connect(lambda:self.SpectroSliders(self.equalizers[11], 'max'))
        self.comboBox.currentTextChanged.connect(lambda:self.spectro())
        self.comboBox.currentTextChanged.connect(lambda:self.FourierSpectrogram())


    def new_window(self):
        from another import Ui_MainWindow2
        self.window=Ui_MainWindow2()
        self.window.show()

    def readsignal(self):
        self.fname=QtGui.QFileDialog.getOpenFileName(self,' txt or CSV or xls',"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)")
        self.path=self.fname[0]
        self.comboBox.show()
        if (self.fname[0].endswith('.wav')):

            for i in range(0,10):
                self.equalizers[i].show()
            self.data,self.fs = librosa.load(os.path.basename(self.path),sr = None, mono = True,offset = 0.0,duration = None)
            self.Fourier()

        else:
            for i in range(0,10):
                self.equalizers[i].hide()
            self.data.append(np.genfromtxt(self.path))
    
    def opensignal(self):
        self.readsignal()
        
        if (self.fname[0].endswith('.wav')):
            self.counter+=1

            self.signals[0].clear()
            self.signals[0].plot(self.data)
            self.signals[0].plotItem.getViewBox().setLimits(xMin=0,xMax=len(self.data))
           
            plt.specgram(self.data, Fs= self.fs, cmap= self.comboBox.currentText())
            plt.savefig('spectro1.png', dpi=300, bbox_inches='tight')
            self.spectrogram[0].setPixmap(QtGui.QPixmap('spectro1.png'))
            plt.close(None)
            self.spectrogram[0].show() 
            self.signals[0].show()
            self.checkBox[0].setChecked(True)
            self.checkBox[2].setChecked(True)
        else: 
            self.counter+=1
            self.n.append(0)
            self.nn.append(0)
            # self.h.append(0)
            x = self.counter
            # self.xmin.append(0)
            # self.xmax.append(0)
            self.speed.append(1)
            self.scrollrate.append(1)
            self.data_line.append(self.signals[self.counter % 3].plot(self.data[self.counter], name="mode2"))
            self.signals[self.counter%3].plotItem.getViewBox().setLimits(xMin=0,xMax=len(self.data[self.counter]))
            self.pen = pg.mkPen(color=(255, 0, 0))
            # Set timer 
            self.timer.append(pg.QtCore.QTimer())
            # Timer signal binding update_data function
            x = self.counter
            if x%3 == 0:
                self.timer[x].timeout.connect(lambda: self.update_data1(x))
                self.timer[x].start(50)
            if x%3 == 1:
                self.timer[x].timeout.connect(lambda: self.update_data2(x)) 
                self.timer[x].start(50)
            if x%3 == 2:
                self.timer[x].timeout.connect(lambda: self.update_data3(x))
                self.timer[x].start(50)
            # The timer interval is 50ms, which can be understood as refreshing data once in 50ms
            #self.timer1.start(50)
            self.signals[x%3].show()
            self.checkBox[x%3].show()
            self.checkBox[x%3].setChecked(True)

        
    def SpectroSliders(self, equalizer, current):
        self.Current[current] = int(equalizer.value())
        self.FourierSpectrogram()
        

    def Fourier(self):
        
      
        self.Amplitude = abs(scipy.fft.fft(self.data)) #the y axis of fft plot (amplitudes)
        self.CopyOfAmplitudes = abs(scipy.fft.fft(self.data))
        self.Frequencies = scipy.fft.fftfreq(len(self.Amplitude), (1.0/self.fs)) #the x axis of fft plot (frequencies)
        self.Phase = np.angle(scipy.fft.fft(self.data))
        self.Complex= scipy.fft.fft(self.data)
     

    def update(self,index):
        index1= list(self.Frequencies).index((0*max(self.Frequencies)/10))
        index2=math.floor((list(self.Frequencies).index(max(self.Frequencies))/10))
        Band=index2-index1
        for i in range(10,12):
            self.equalizers[i].show()
      

        
        for i in range(((index1+(Band*index))+1),((index2+(Band*index)))):
            self.Amplitude[i]=self.equalizers[index].value() * self.CopyOfAmplitudes[i]
            self.Amplitude[-i]=self.equalizers[index].value() * self.CopyOfAmplitudes[-i]
            self.Complex[i] = self.Amplitude[i]*(math.cos(self.Phase[i]))+self.Amplitude[i]*(math.sin(self.Phase[i]))*1j
            self.Complex[-i] = self.Amplitude[-i]*(math.cos(self.Phase[-i]))+self.Amplitude[-i]*(math.sin(self.Phase[-i]))*1j
      
        self.InversedData =scipy.fft.ifft(self.Complex)
        self.spectroSlider=[0,max(self.Frequencies)/5,2*max(self.Frequencies)/5,3*max(self.Frequencies)/5,4*max(self.Frequencies)/5,max(self.Frequencies)]
       
        self.FourierSpectrogram()
        self.signals[2].clear()
        self.signals[2].plot(self.InversedData.real)
        self.signals[2].plotItem.getViewBox().setLimits(xMin=0,xMax=len(self.InversedData))
        self.signals[2].show()

        
    def FourierSpectrogram(self) :  
        plt.specgram(self.data, Fs=self.fs ,cmap=self.comboBox.currentText())
        plt.savefig('spectro1.png', dpi=300, bbox_inches='tight')
        self.spectrogram[0].setPixmap(QtGui.QPixmap('spectro1.png'))
        # print(self.comboBox.currentText())
        self.spectrogram[2].show()
        plt.specgram(self.InversedData.real, Fs=self.fs ,cmap=self.comboBox.currentText())
        plt.ylim((self.spectroSlider[self.Current['min']], self.spectroSlider[self.Current['max']]))
        plt.savefig('spectro2.png', dpi=300, bbox_inches='tight')
        self.spectrogram[2].setPixmap(QtGui.QPixmap('spectro2.png'))
        plt.close(None)
         
 

    # Data shift left
    def update_data1(self,index):
        if self.n[index] < len(self.data[index]):
            if self.n[index] < 1000 :    
                self.n[index] += 10 * self.speed[index]
                self.data_line[index].setData(self.data[index][0 : self.n[index]])
                self.signals[index%3].plotItem.setXRange(0, self.r[index] , padding=0)
                self.xmin[index]= 0
                self.xmax[index]= self.r[index]
            
            else :
                self.nn[index] +=  10 * self.speed[index]
                self.n[index] += 10 * self.speed[index]
                self.data_line[index].setData(self.data[index][0 : self.n[index]])
                self.signals[index%3].plotItem.setXRange(self.nn[index],self.r[index] +self.nn[index] , padding=0)
                self.xmin[index] = self.nn[index]
                self.xmax[index] = self.r[index] +self.nn[index]

            self.z[index] = 1
            
        else :
            self.data_line[index].setData(self.data[index][0 : self.n[index]])
            self.signals[index%3].plotItem.setXRange(0 , len(self.data[index])* self.z[index] , padding=0)
            self.xmin[index] = 0 
            self.xmax[index] = len(self.data[index])* self.z[index]

    def update_data2(self,index):
        if self.n[index] < len(self.data[index]):
            if self.n[index] < 1000 :    
                self.n[index] += 10 * self.speed[index]
                self.data_line[index].setData(self.data[index][0 : self.n[index]])
                self.signals[index%3].plotItem.setXRange(0, self.r[index] , padding=0)
                self.xmin[index]= 0
                self.xmax[index]= self.r[index]
            
            else :
                self.nn[index] +=  10 * self.speed[index]
                self.n[index] += 10 * self.speed[index]
                self.data_line[index].setData(self.data[index][0 : self.n[index]])
                self.signals[index%3].plotItem.setXRange(self.nn[index],self.r[index] +self.nn[index] , padding=0)
                self.xmin[index] = self.nn[index]
                self.xmax[index] = self.r[index] +self.nn[index]

            self.z[index] = 1
            
        else :
            self.data_line[index].setData(self.data[index][0 : self.n[index]])
            self.signals[index%3].plotItem.setXRange(0 , len(self.data[index])* self.z[index] , padding=0)
            self.xmin[index] = 0 
            self.xmax[index] = len(self.data[index])* self.z[index]



    def update_data3(self,index):
        if self.n[index] < len(self.data[index]):
            if self.n[index] < 1000 :    
                self.n[index] += 10 * self.speed[index]
                self.data_line[index].setData(self.data[index][0 : self.n[index]])
                self.signals[index%3].plotItem.setXRange(0, self.r[index] , padding=0)
                self.xmin[index]= 0
                self.xmax[index]= self.r[index]
            
            else :
                self.nn[index] +=  10 * self.speed[index]
                self.n[index] += 10 * self.speed[index]
                self.data_line[index].setData(self.data[index][0 : self.n[index]])
                self.signals[index%3].plotItem.setXRange(self.nn[index],self.r[index] +self.nn[index] , padding=0)
                self.xmin[index] = self.nn[index]
                self.xmax[index] = self.r[index] +self.nn[index]

            self.z[index] = 1
            
        else :
            self.data_line[index].setData(self.data[index][0 : self.n[index]])
            self.signals[index%3].plotItem.setXRange(0 , len(self.data[index])* self.z[index] , padding=0)
            self.xmin[index] = 0 
            self.xmax[index] = len(self.data[index])* self.z[index]



    def spectro(self):
 
        if not (self.fname[0].endswith('.wav')):
            index = (len(self.data) - 1) - ((len(self.data)-1)%3)

            for i in range (0,3):
                if (self.checkBox[i].isChecked()==True):
                    self.spectrogram[i].show()
                    if i==0:
                        print(self.comboBox.currentText())
                
                        plt.specgram(self.data[index], Fs= 250 ,cmap=self.comboBox.currentText())
                    elif i == 1:    
                        if (len(self.data ) - 1 - index >= 1):
                            plt.specgram(self.data[index + 1], Fs= 250 ,cmap=self.comboBox.currentText())
                        else:
                            plt.specgram(self.data[index - 2], Fs= 250,cmap=self.comboBox.currentText() )

                    else:
                        if (len(self.data) - 1 - index == 2):
                            plt.specgram(self.data[index + 2], Fs= 250,cmap=self.comboBox.currentText() )

                        else:
                            plt.specgram(self.data[index - 1], Fs= 250,cmap=self.comboBox.currentText() )
                    plt.savefig('spectro'+str(i)+'.png', dpi=300, bbox_inches='tight')
                    self.spectrogram[i].setPixmap(QtGui.QPixmap('spectro'+str(i)+'.png'))
                    plt.close(None)



    def sounds(self):
 
        
        QtMultimedia.QSound.play(self.path)
        #pass
       
    def wave(self):
        self.count+=1
        wavio.write("new"+str(self.count)+".wav", self.InversedData.real, self.fs, sampwidth=2)
        self.sound = QSound("new"+str(self.count)+".wav")
        self.sound.play()

        
    def pausee(self):
        for i in range (0,3):
            if (self.checkBox[i].isChecked()==True):
                if self.timer[i].isActive():
                    self.timer[i].stop()

    def playy(self):
        for i in range (0,3):
            if (self.checkBox[i].isChecked()==True):
                if self.timer[i].isActive()==False:
                    self.timer[i].start()
        
    def zoomin(self):
        for i in range (0,3):
            if (self.checkBox[i].isChecked()==True):
                print(bool(self.checkBox[2]))
                self.signals[i].plotItem.getViewBox().scaleBy(x=0.5,y=1)
                self.r[i]=self.r[i]*0.5
                self.z[i] = self.z[i] * 0.5
                # self.scrollrate[i] *=  0.5
                # self.scrollrate[i]=int(self.scrollrate[i])
      
    def zoomout(self):
        for i in range (0,3):
            if (self.checkBox[i].isChecked()==True):
                self.signals[i].plotItem.getViewBox().scaleBy(x=2,y=1)
                self.r[i]=self.r[i]*2
                self.z[i] = self.z[i] * 2
                # self.scrollrate[i] *=  2

      
    def scrlleft(self):
        for i in range (0,3):
            if (self.checkBox[i].isChecked()==True):
                self.signals[i].plotItem.getViewBox().translateBy(x=-100  ,y=0)
                
      
    def scrlright(self):
        for i in range (0,3):
            if (self.checkBox[i].isChecked()==True):
                self.signals[i].plotItem.getViewBox().translateBy(x=100  ,y=0)
                
    def SpeedUp(self):

        for i in range (0,3):
            if (self.checkBox[i].isChecked()==True):
                self.speed[i]  *=  2

    def SpeedDown(self):

       for i in range (0,3):
            if (self.checkBox[i].isChecked()==True):
                self.speed[i]  *=  0.5
                self.speed[i] = int(self.speed[i])
                plt.plot(spectrogramData,linewidth=0.5,scalex=True)



                

#     
    def savepdf(self):
        fig=plt.figure(figsize=(1000, 1000))
        if (self.fname[0].endswith('.wav')):
            plt.subplot(2,2,1)
            plt.plot(self.data,linewidth=0.5,scalex=True)
            plt.subplot(2,2,2)
            plt.specgram(self.data, Fs= self.fs, cmap= self.comboBox.currentText())
            plt.subplot(2,2,3)
            plt.plot(self.InversedData,linewidth=0.5,scalex=True)
            plt.subplot(2,2,4)
            plt.specgram(self.InversedData.real, Fs= self.fs, cmap= self.comboBox.currentText())


        if not (self.fname[0].endswith('.wav')):
            index = (len(self.data) - 1) - ((len(self.data)-1)%3)
            spectrogramData = []
            for i in range (0,3):
                if (self.checkBox[i].isChecked()==True):
        
                    if i == 0:
                        plt.subplot(3,2,1)
                        spectrogramData = list(self.data[index][0:]) 
                        plt.plot(spectrogramData,linewidth=0.5,scalex=True)
                        plt.subplot(3,2,2)
                    elif i == 1:   
                        
                        if (len(self.data ) - 1 - index >= 1):
                            plt.subplot(3,2,3)
                            spectrogramData = list(self.data[index+1][0:])
                            plt.plot(spectrogramData,linewidth=0.5,scalex=True)
                            plt.subplot(3,2,4)
                        else:
                            plt.subplot(3,2,3)
                            spectrogramData = list(self.data[index-2][0:])
                            plt.plot(spectrogramData,linewidth=0.5,scalex=True)
                            plt.subplot(3,2,4)
                    else:
                        if (len(self.data) - 1 - index == 2):
                            plt.subplot(3,2,5)
                            spectrogramData = list(self.data[index+2][0:])
                            plt.plot(spectrogramData,linewidth=0.5,scalex=True)
                            plt.subplot(3,2,6)
                        else:
                            plt.subplot(3,2,5)
                            spectrogramData = list(self.data[index-1][0:])
                            plt.plot(spectrogramData,linewidth=0.5,scalex=True)
                            plt.subplot(3,2,6)
                    plt.specgram(spectrogramData, Fs= 250)

      
        plt.subplots_adjust(bottom=0.1,right=0.9,top=1.0)
        plt.show()
        plt.close()
        fn,_=QtWidgets.QFileDialog.getSaveFileName(self,"Export PDF",None,"PDF files(.pdf);;AllFiles()")
        if fn:
            if QtCore.QFileInfo(fn).suffix()=="":
                fn+=".pdf"
                fig.savefig(fn)
                    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "viridis"))
        self.comboBox.setItemText(1, _translate("MainWindow", "plasma"))
        self.comboBox.setItemText(2, _translate("MainWindow", "turbo"))
        self.comboBox.setItemText(3, _translate("MainWindow", "cividis"))
        self.comboBox.setItemText(4, _translate("MainWindow", "BuPu"))
        self.checkBox[1].setText(_translate("MainWindow", "signal-2"))
        self.checkBox[1].setShortcut(_translate("MainWindow", "2"))
        self.checkBox[2].setText(_translate("MainWindow", "signal-3"))
        self.checkBox[2].setShortcut(_translate("MainWindow", "3"))
        self.checkBox[0].setText(_translate("MainWindow", "signal-1"))
        self.checkBox[0].setShortcut(_translate("MainWindow", "1"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSignal_tools.setTitle(_translate("MainWindow", "Signal tools"))
        self.menuPlay_navigate.setTitle(_translate("MainWindow", "Play and navigate "))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+o"))
        self.actionzoom_in.setText(_translate("MainWindow", "Zoom-in"))
        self.actionzoom_in.setShortcut(_translate("MainWindow", "Up"))
        self.actionzoom_out.setText(_translate("MainWindow", "Zoom-out"))
        self.actionzoom_out.setShortcut(_translate("MainWindow", "Down"))
        self.actionSpectrogram.setText(_translate("MainWindow", "Spectrogram"))
        self.actionSpectrogram.setShortcut(_translate("MainWindow", "S"))
        self.actionPlay.setText(_translate("MainWindow", "Play"))
        self.actionPlay.setShortcut(_translate("MainWindow", "Space"))
        self.actionPause.setText(_translate("MainWindow", "Pause"))
        self.actionPause.setShortcut(_translate("MainWindow", "Shift+Space"))
        self.actionBackward.setText(_translate("MainWindow", "Backward"))
        self.actionBackward.setShortcut(_translate("MainWindow", "Left"))
        self.actionForward.setText(_translate("MainWindow", "Forward"))
        self.actionForward.setShortcut(_translate("MainWindow", "Right"))
        self.actionSave_as_pdf.setText(_translate("MainWindow", "Save as pdf"))
        self.actionSave_as_pdf.setShortcut(_translate("MainWindow", "Ctrl+S"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
