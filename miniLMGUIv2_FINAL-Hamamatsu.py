import os
import pylab as pl
import numpy as np
import sys
sys.path.append("C:\Program Files\Micro-Manager-1.4")
from PyQt4 import QtGui, QtCore 
from miniLM_GUILayoutv2FINAL import Ui_MainWindow # This is the external layout file
import MMCorePy
import time
import datetime
import qimage2ndarray as q2
from PIL import Image
import pyqtgraph as pg

#########################################################################################################
#                                                 Mini LM GUI                                           #
#   GUI to control the light imaging of the miniLM. Hamamatsu Flash 4 controlled by micromanager.       # 
#   (This might need review as a bit flakey.) Allows single imaging + saving, continuous live imaging,  #
#   with or without saving data (as 8bit TIFF). User can set exposure time, external trigger, and has   #
#   control over zoom, contrast and brightness in the image display.                                    #
#                                                                                                       #
#########################################################################################################

class Window(QtGui.QMainWindow, Ui_MainWindow):
    
    # Define signals used 
    arraySignal = QtCore.pyqtSignal(np.ndarray)
    histSignal = QtCore.pyqtSignal()
    saveFolderSignal = QtCore.pyqtSignal(str)
    imageCounterSignal = QtCore.pyqtSignal(int)
    zoomFactorSignal = QtCore.pyqtSignal(float)
 
    # Initialise GUI using the external layout file
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.fileroot = os.getcwd() # Get working directory and show as folder that images are saved to
        self.fileLocationTextBrowser.setText(str(self.fileroot))
        # Start worker thread and initialise 
        self.objThread = QtCore.QThread()    
        self.arraySignal.connect(self.showImage)
        self.histSignal.connect(self.showHistogram)
        self.imageCounterSignal.connect(self.updateImageCounter)
        self.saveFolderSignal.connect(self.changeSaveDirectory)
        self.liveObject = workerObject(self.liveImage)
        self.liveObject.moveToThread(self.objThread)

        self.scaleFactor = 0.315 # This is for Flash 4 with 2048 pixels - would be better to read in chip size and calculate!
        self.zoomInPushButton.setEnabled(False)  # Disable buttons that are meaningless without image
        self.zoomOutPushButton.setEnabled(False)
        self.minHorizontalSlider.setEnabled(False)
        self.maxHorizontalSlider.setEnabled(False)
        self.brightnessHorizontalSlider.setEnabled(False)
        self.saveButton.setEnabled(False)
        #initialise variables needed straight away
        self.greyscaleFactor = [0, 255]
        self.sValueInitial = 0
        self.ExpTime = 100
        self.expTimeSpinBox.setValue(self.ExpTime)
        #initialise micromanager and camera
        self.mmc = MMCorePy.CMMCore()
        self.mmc.loadDevice("Camera", "HamamatsuHam", "HamamatsuHam_DCAM")
        self.mmc.initializeAllDevices()
        self.mmc.setCameraDevice("Camera")
        self.mmc.setExposure(self.ExpTime)
        self.mmc.setProperty("Camera", "OUTPUT TRIGGER KIND[0]", "EXPOSURE")
        self.mmc.setProperty("Camera", "OUTPUT TRIGGER POLARITY[0]", "POSITIVE")
        self.mmc.setProperty("Camera", "TRIGGER SOURCE", "INTERNAL")
        self.mmc.setProperty("Camera", "TriggerPolarity", "POSITIVE")
    


        
          ########################################################
          ####### Button connections in the Window class #########
          ########################################################
 
# Quit program
        self.quitPushButton.clicked.connect(self.stopImaging)
        self.quitPushButton.clicked.connect(QtGui.QApplication.instance().quit)
        self.quitPushButton.clicked.connect(self.close)

# Snap single image
        self.snapButton.clicked.connect(self.snapImage)
        self.snapButton.clicked.connect(self.enableZoomButtons)
        self.saveButton.clicked.connect(self.saveImage)

# Set exposure time
        self.expTimeSpinBox.valueChanged.connect(self.setExpTime)

# Wait for external trigger
        self.externalTriggerCheckBox.stateChanged.connect(self.setExtTrigger)
        
# Live imaging
        self.liveButton.clicked.connect(self.liveThread)
        self.liveButton.clicked.connect(self.disableButtons)
        self.liveButton.clicked.connect(self.enableZoomButtons)
        self.stopButton.clicked.connect(self.stopImaging)
        self.stopButton.clicked.connect(self.enableButtons)
        self.dirSelectionToolButton.clicked.connect(self.setSaveDirectory)

# Zoom image and other display control

        self.zoomInPushButton.clicked.connect(self.zoomInFactor)
        self.zoomOutPushButton.clicked.connect(self.zoomOutFactor)
        self.zoomFactorSignal.connect(self.scaleImage)
        self.minHorizontalSlider.valueChanged.connect(self.changeMinValue)
        self.maxHorizontalSlider.valueChanged.connect(self.changeMaxValue)
        self.brightnessHorizontalSlider.valueChanged.connect(self.changeBrightness)
        self.resetPushButton.clicked.connect(self.resetHistogram)


          ########################################################
          ############ Methods of Window class ###################
          ########################################################

# Single Image

    def snapImage(self):
        self.saveButton.setEnabled(True)
        self.mmc.snapImage()
        big_array = self.mmc.getImage()
        array = big_array/256
      #  array = np.random.randint(255, size=(2048, 2048)) # this would be the array generated by the camera
        self.showImage(array)
        self.tempArray = array
        self.showHistogram()
        return (self.tempArray)
        
    def saveImage(self):
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save Image', 'Image_'+time.strftime('%Y%m%d-%H%M%S')+'.tiff')
        if fileName:  # if not using if here, shell shows error when user clicks cancel
            im = Image.fromarray(self.tempArray.astype('uint8'))
            im.save(str(fileName))

# Zoom --------------------------------------------------

    def zoomInFactor(self):
        self.zoomFactorSignal.emit(1.25)
                                       
    def zoomOutFactor(self):
       self.zoomFactorSignal.emit(0.80)           

    @QtCore.pyqtSlot(float)
    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageDisplayLabel.resize(self.scaleFactor * self.imageDisplayLabel.pixmap().size())
        self.zoomInPushButton.setEnabled(self.scaleFactor < 4)
        self.zoomOutPushButton.setEnabled(self.scaleFactor > 0.35)
        return self.scaleFactor
        
    def enableZoomButtons(self):
        self.zoomInPushButton.setEnabled(True)
        self.zoomOutPushButton.setEnabled(True)
        self.minHorizontalSlider.setEnabled(True)
        self.maxHorizontalSlider.setEnabled(True)
        self.brightnessHorizontalSlider.setEnabled(True)

# Change imaging parameters ----------------------------------

    def setExpTime(self):
        #print self.expTimeSpinBox.value()   # There may be a better way to do this - if typing 100 this sets it to 1, 10, then 100
        self.mmc.setExposure(self.expTimeSpinBox.value())
        self.ExpTime = self.expTimeSpinBox.value()

    def setExtTrigger(self):
        if self.externalTriggerCheckBox.isChecked() == True:
            self.mmc.setProperty("Camera","TRIGGER SOURCE","EXTERNAL")
        else:
            self.mmc.setProperty("Camera","TRIGGER SOURCE","INTERNAL")

# Change display parameters ----------------------------------

    def changeMinValue(self):
        self.greyscaleFactor[0] = self.minHorizontalSlider.value()
        self.showImage(self.tempArray)
        self.updateHistogramRange()
        return (self.greyscaleFactor)

    def changeMaxValue(self):
        self.greyscaleFactor[1] = self.maxHorizontalSlider.value()
        self.showImage(self.tempArray)
        self.updateHistogramRange()
        return (self.greyscaleFactor)

    def changeBrightness(self):
        sValue = self.brightnessHorizontalSlider.value()
        moveFactor = self.sValueInitial - sValue
        self.greyscaleFactor[0] = self.greyscaleFactor[0] + moveFactor
        self.greyscaleFactor[1] = self.greyscaleFactor[1] + moveFactor 
        self.sValueInitial = sValue
        self.showImage(self.tempArray)
        self.updateHistogramRange()
        return (self.greyscaleFactor)
        
    def resetHistogram(self):
        self.showImage(self.tempArray)
        self.minHorizontalSlider.setSliderPosition(0)
        self.maxHorizontalSlider.setSliderPosition(255)
        self.brightnessHorizontalSlider.setSliderPosition(0)
        self.greyscaleFactor = [0, 255] # Not the most efficient as the 3 lines above activate 3 methods that all change greyscaleFactor
        self.updateHistogramRange()
        return (self.greyscaleFactor)
    
 # Display histogram --------------------------------------------      

    def displayHistogram(self):
        # Get histogram
        self.hist = np.histogram(self.tempArray, range(0, 256)) # computes histogram of the image array
        self.Histogram.setYRange(0, self.hist[0].max()+0.1*self.hist[0].max(), 0) # sets graphs y axis max to max pixel value + 10%
        bins = self.hist[1]  # reduce number of bins by one to match dimensions for plot
        reducedBins = bins[:-1]
        # Prepare data for line plot
        x = range(self.greyscaleFactor[0], self.greyscaleFactor[1])
        gradient = self.hist[0].max()/(self.greyscaleFactor[1]- self.greyscaleFactor[0])
        y = gradient * (np.array(x) - self.greyscaleFactor[0])
        # Plot histogram and line representing part of histogram shown in image
        self.Histogram.plot(reducedBins, self.hist[0])
        self.linePlot = self.Histogram.plot(x, y) 
        
    def updateHistogramRange(self):
        x = range(self.greyscaleFactor[0], self.greyscaleFactor[1])
        gradient = self.hist[0].max()/(self.greyscaleFactor[1]- self.greyscaleFactor[0])
        y = gradient * (np.array(x) - self.greyscaleFactor[0])
        self.Histogram.removeItem(self.linePlot)
        self.linePlot = self.Histogram.plot(x, y)

        
 # Enable/Disable buttons when required (i.e. during live imaging)  

    def enableButtons(self):
        self.saveCheckBox.setEnabled(True)
        self.externalTriggerCheckBox.setEnabled(True)
        self.expTimeSpinBox.setEnabled(True)
        self.liveButton.setEnabled(True)
        self.dirSelectionToolButton.setEnabled(True)
        self.snapButton.setEnabled(True)
        self.saveButton.setEnabled(True)

    def disableButtons(self):
        self.saveCheckBox.setEnabled(False)
        self.externalTriggerCheckBox.setEnabled(False)
        self.expTimeSpinBox.setEnabled(False)
        self.liveButton.setEnabled(False)
        self.dirSelectionToolButton.setEnabled(False)
        self.snapButton.setEnabled(False)
        self.saveButton.setEnabled(False)

# Save directory -----------------------------------------------

    def setSaveDirectory(self):
        self.fileroot = QtGui.QFileDialog.getExistingDirectory(self, 'Select Directory')
        if self.fileroot:
            self.fileLocationTextBrowser.setText(str(self.fileroot))
            return self.fileroot
        
    # Updates display of where images are being saved
    @QtCore.pyqtSlot(str)
    def changeSaveDirectory(self, saveFolder):
        self.fileLocationTextBrowser.setText(saveFolder)

####### Live Imaging Stuff  ############
        
    # Declaring slots/signals explicitly is essential for passing data from one thread to another
    # Convert numpy array to greyscale image, add to imageDisplay label and resize according to scaleFactor
    @QtCore.pyqtSlot(np.ndarray) 
    def showImage(self, filename):
        imageOfArray = q2.gray2qimage(filename, self.greyscaleFactor)
        self.imageDisplayLabel.setPixmap(QtGui.QPixmap.fromImage(imageOfArray))
        self.imageDisplayLabel.resize(self.scaleFactor * self.imageDisplayLabel.pixmap().size())

    @QtCore.pyqtSlot()
    def showHistogram(self):
        self.Histogram.clear()
        self.displayHistogram()
    
    @QtCore.pyqtSlot(int)
    def updateImageCounter(self, number):
        self.ImageNumberCounter.display(number)

    # liveImaging method - to be moved to workerThread inside workerObject instance
    def liveImage(self):  
        nAcquisition = 0
        # Make save directory with date and time if user selects to save data
        if self.saveCheckBox.isChecked() == True:
            if self.fileroot:
                timeStamp = time.strftime('%Y%m%d-%H%M%S')
                saveFolder = os.path.join(str(self.fileroot),str(timeStamp))
                if not os.path.exists(saveFolder):
                    os.makedirs(saveFolder)
                self.saveFolderSignal.emit(saveFolder)

        # Continuous image acquisition           
        while self.flag == True:
            self.mmc.snapImage()
            big_array = self.mmc.getImage()
            array = big_array/256
            self.tempArray = array
            self.arraySignal.emit(self.tempArray)
            self.histSignal.emit()
            self.imageCounterSignal.emit(nAcquisition)
            nAcquisition = nAcquisition + 1
            time.sleep((self.ExpTime + 50)/1000.0)
            # Save images
            if self.saveCheckBox.isChecked() == True:
                fileName = 'Image_'+str(nAcquisition)+'.tiff' 
                fullPath = os.path.join(saveFolder,fileName)
                fullFileName = os.path.abspath(fullPath)
                im = Image.fromarray(self.tempArray.astype('uint8'))
                im.save(str(fullFileName))

    # Create instance of workerObject and move liveImaging there to be executed, connect relevant signals
    def liveThread(self):
        self.flag = True # Updating the flag allows to stop the program (although I suspect signals may also work)
##        self.arraySignal.connect(self.showImage)
##        self.histSignal.connect(self.showHistogram)
##        self.imageCounterSignal.connect(self.updateImageCounter)
##        self.saveFolderSignal.connect(self.changeSaveDirectory)
##        liveObject = workerObject(self.liveImage)
##        liveObject.moveToThread(self.objThread)
        self.objThread.start()
        self.liveObject.start.emit()
        #self.liveObject = liveObject
        self.liveObject.deleteLater
        
    def stopImaging(self):
        self.flag = False
        if self.liveButton.isChecked() == True:
            self.liveButton.toggle()

  
####################### worker object class ##########################
        
class workerObject(QtCore.QObject):

    start = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()
      
    def __init__(self, function, *args):
        QtCore.QObject.__init__(self, parent=None)
        self.function = function
        self.args = args
        self.start.connect(self.run) # Start the run method when the start is called from liveThread method in main thread
 
    @QtCore.pyqtSlot()  # Explicitly decorates the run method as a pyqt slot 
    def run(self):
        self.function()#(self.args)
        self.finished.emit()   # Not sure what this does - but doesn't work without?

      
############################# MAIN ##################################

def main():
    
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()

    
