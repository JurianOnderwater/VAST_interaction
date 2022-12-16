import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
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

from image_acquisition.micromanager import Acquire


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()

        self.Acquirer = Acquire()
        self.magnificaitons_list = list(self.Acquirer.turret_dict.keys())
        self.multi_channel = QCheckBox('Use Fluoresence')
        self.magnification_level = QComboBox()
        self.magnification_level.addItems(self.magnificaitons_list)
        self.test_label = QLabel('Acquisition name:')
        self.acquisition_name = QLineEdit()
        self.light_level = QSlider(Qt.Horizontal)
        self.start = QPushButton('Start')
        
        widgets = [
            self.multi_channel,
            self.magnification_level,
            self.test_label,
            self.acquisition_name,
            self.light_level,
            self.start,
            ]

        for w in widgets:
            layout.addWidget(w)

        # layout.
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()