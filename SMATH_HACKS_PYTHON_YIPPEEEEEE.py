# SMATH_HACKS PYTHON YIPPEEEEEE

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

f = open("data.txt", "r")
dataValues = f.readlines()

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Plant Habitibility Calculator")

        layout = QVBoxLayout()
        self.plantDropdown = QComboBox()
        self.plantDropdown.addItems(["None Selected", "Oak Tree", "Grass", "Corn", "Rice", "Soybeans"])
        tempLabel = QLabel("Temperature: " + dataValues[0].strip('\n'))
        humLabel = QLabel("Humidity: " + dataValues[1].strip('\n'))
        self.surviveLabel = QLabel("No plant selected.")

        self.plantDropdown.activated.connect(self.switch)
        self.plantDropdown.currentIndexChanged.connect(self.switch)
        

        widgets = [
            self.plantDropdown,
            tempLabel,
            humLabel,
            self.surviveLabel
        ]

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def switch(self, index):
        if self.plantDropdown.currentIndex() == 0:
            self.surviveLabel.setText("No plant selected.")
        elif self.plantDropdown.currentIndex() == 1:
            self.surviveLabel.setText("Oak trees could, uh, probably survive?")
        elif self.plantDropdown.currentIndex() == 2:
            self.surviveLabel.setText("Look, I dunno if grass can survive, I'm just the intern.")
        elif self.plantDropdown.currentIndex() == 3:
            self.surviveLabel.setText("Corn can. Maybe survive? Kinda seems a bit hot though.")
        elif self.plantDropdown.currentIndex() == 4:
            self.surviveLabel.setText("I think you need a little more water for rice.")
        elif self.plantDropdown.currentIndex() == 5:
            self.surviveLabel.setText("I know nothing about soybeans, sorry.")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()