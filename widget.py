import sys
from image_acquisition.micromanager import Acquire
from file_sharing.transfer import Transfer
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSlider,
    QProgressBar,
    QVBoxLayout,
    QWidget,
)

# Subclass QMainWindow to customize application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VAST Acquisition")

        layout = QVBoxLayout()

        self.Acquirer = Acquire(path=r"\test", name="pycromanager_test")
        self.Transferer = Transfer()
        self.magnifications_list = list(mag for mag in self.Acquirer.turret_dict.keys())
        self.ticks = [50, 100, 150, 200]

        self.multi_channel = QCheckBox('Use Fluoresence')

        self.magnification_level = QComboBox()
        self.magnification_level.addItems(str(x) for x in self.magnifications_list)
        self.magnification_level.currentTextChanged.connect(self.magnification_value_change)

        self.test_label = QLabel('Acquisition name:')
        # self.acquisition_name = QLineEdit()
        self.acquisition_name = QLineEdit(self.Acquirer.name) # Don't hardcode here, results in typeError

        self.light_level = QSlider(Qt.Horizontal)
        # self.light_level.setMinimum(0)
        # self.light_level.setMaximum(255)
        self.light_level.setRange(min: 0, max: 255)
        self.light_level.setTickPosition(QSlider.TicksAbove)
        self.light_level.setTickInterval(50)
        self.light_level.valueChanged.connect(self.light_value_change)

        self.start = QPushButton('Start Acquisition')
        self.start.setCheckable(True)
        self.start.clicked.connect(self.start_acquisition)

        # self.progress_bar = QProgressBar()
        # self.progress_bar.setRange(0, self.Acquirer.NUM_IMAGES)
        # self.progress_bar.setValue(self.Acquirer.progress)

        widgets = [
            self.multi_channel,
            self.magnification_level,
            self.test_label,
            self.acquisition_name,
            self.light_level,
            self.start,
            ]

        for w in widgets:           # lotta w's out here
            layout.addWidget(w)

        # layout
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def light_value_change(self):
        """
        Change the brightness of the lamp used in the microscope
        """
        brightness = self.light_level.value()
        self.Acquirer.set_brightness(val=brightness)

    def magnification_value_change(self):
        """
        Change the magnification factor used in the microscope
        """
        magnification = self.magnification_level.currentText()
        self.Acquirer.set_zoom(mag=magnification)

    def start_acquisition(self):
        """
        Start the capture images and transfer them to the server
        """
        self.Acquirer.capture_series(num_time_points=5, time_interval=1)
        self.Transferer.transfer()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()