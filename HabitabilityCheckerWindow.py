# SMATH_HACKS PYTHON YIPPEEEEEE

# Imports
import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

# Defining txt file
dataTxtFile = "SensorData.txt"

# Defining plant data
oakData = [-5, 35, 40, 50]
grassData = [6, 35, 50, 70]
cornData = [10, 30, 50, 80]
riceData = [10, 38, 50, 90]
soyData = [10, 30, 40, 75]

# Making main window subclass to be able to customize window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting window title to project title
        self.setWindowTitle("Plant Habitability Calculator")

        # Initial values for temperature and humidity so things don't get errors
        self.temp = 0.0
        self.hum = 0.0

        # Making all window elements
        layout = QVBoxLayout()
        self.plantDropdown = QComboBox()
        self.plantDropdown.addItems(["None Selected", "Oak Tree", "Grass", "Corn", "Rice", "Soybeans"])
        self.tempLabel = QLabel("Temperature: Loading...")
        self.humLabel = QLabel("Humidity: Loading...")
        self.surviveLabel = QLabel("No plant selected.")
        self.rangeLabel = QLabel("")

        # Updating dropdown menu selections
        self.plantDropdown.activated.connect(self.switch)
        self.plantDropdown.currentIndexChanged.connect(self.switch)
        
        # Adding elements to the screen
        widgets = [
            self.plantDropdown,
            self.tempLabel,
            self.humLabel,
            self.surviveLabel,
            self.rangeLabel
        ]
        for w in widgets:
            layout.addWidget(w)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Adding loop so temperature and humidity updates if the txt file has updated
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    # Switches text of window labels when different dropdown menu selections are made
    def switch(self):
        text = "Error"
        rangeText = "Error"
        dataList = [-1, -1, -1, -1]

        # Checks what menu item is picks and changes variables accordingly
        if self.plantDropdown.currentIndex() == 0:
            text = "No plant selected."
            self.rangeLabel.setText("")
        elif self.plantDropdown.currentIndex() == 1:
            if self.temp > oakData[0] and self.temp < oakData[1] and self.hum > oakData[2] and self.hum < oakData[3]:
                text = "Oak trees could survive here!"
            else:
                text = "Oak trees could not survive here."
            rangeText = "Oak trees have"
            dataList = oakData
        elif self.plantDropdown.currentIndex() == 2:
            if self.temp > grassData[0] and self.temp < grassData[1] and self.hum > grassData[2] and self.hum < grassData[3]:
                text = "Grass could survive here!"
            else:
                text = "Grass could not survive here."
            rangeText = "Grass has"
            dataList = grassData
        elif self.plantDropdown.currentIndex() == 3:
            if self.temp > cornData[0] and self.temp < cornData[1] and self.hum > cornData[2] and self.hum < cornData[3]:
                text = "Corn could survive here!"
            else:
                text = "Corn could not survive here."
            rangeText = "Corn has"
            dataList = cornData
        elif self.plantDropdown.currentIndex() == 4:
            if self.temp > riceData[0] and self.temp < riceData[1] and self.hum > riceData[2] and self.hum < riceData[3]:
                text = "Rice could survive here!"
            else:
                text = "Rice could not survive here."
            rangeText = "Rice has"
            dataList = riceData
        elif self.plantDropdown.currentIndex() == 5:
            if self.temp > soyData[0] and self.temp < soyData[1] and self.hum > soyData[2] and self.hum < soyData[3]:
                text = "Soy beans could survive here!"
            else:
                text = "Soy beans could not survive here."
            rangeText = "Soy beans have"
            dataList = soyData

        # Changing labels to new display
        self.surviveLabel.setText(text)
        if not self.plantDropdown.currentIndex() == 0:
            self.rangeLabel.setText(rangeText + " an ideal temperature range of " + str(dataList[0]) + "°C to " + str(dataList[1]) + "°C, \nand an ideal humidity range of " + str(dataList[2]) + "% to " + str(dataList[3]) + "%.")

    # Updates everything, runs each QTimer loop
    def update(self):
        # Opening txt file and reading last two lines
        f = open(dataTxtFile, "r")
        dataValues = f.readlines()[-2:]

        # Checking if txt file has appropriate number of lines
        if len(dataValues) > 1:
            # Updating temperature and humidity values
            self.temp = float(dataValues[1].strip("\n"))
            self.hum = float(dataValues[0].strip("\n"))

            # Updating text labels
            self.tempLabel.setText("Temperature: " + dataValues[1].strip('\n') + "°C")
            self.humLabel.setText("Humidity: " + dataValues[0].strip('\n') + "%")

            # Checking plant habitability with new values
            self.switch()

# PyQt configuration
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()