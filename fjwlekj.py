import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, Qt

class SoundRecordingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.elapsed_time = 0
        self.is_recording = False

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Sound Recording App')
        self.setGeometry(100, 100, 400, 600)  # Set a taller aspect ratio

        main_layout = QVBoxLayout()

        # Timer label
        self.timer_label = QLabel('00:00', self)
        self.timer_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.timer_label)

        # Buttons layout
        buttons_layout = QHBoxLayout()

        # Record button
        self.record_button = QPushButton(self)
        self.record_button.setIcon(QIcon('rec.png'))  # Replace with your own icon
        self.record_button.clicked.connect(self.toggle_record)
        self.record_button.setFixedSize(100,100)
        buttons_layout.addWidget(self.record_button)

        # Pause button
        self.pause_button = QPushButton(self)
        self.pause_button.setIcon(QIcon('pau.png'))  # Replace with your own icon
        self.pause_button.clicked.connect(self.toggle_pause)
        buttons_layout.addWidget(self.pause_button)

        # Flag button
        self.flag_button = QPushButton(self)
        self.flag_button.setIcon(QIcon('flg.png'))  # Replace with your own icon
        self.flag_button.clicked.connect(self.flag)
        buttons_layout.addWidget(self.flag_button)

        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

        self.show()

    def toggle_record(self):
        if not self.is_recording:
            self.timer.timeout.connect(self.update_timer)
            self.timer.start(1000)  # Update every second
        else:
            self.timer.stop()
        self.is_recording = not self.is_recording

    def toggle_pause(self):
        if self.is_recording:
            self.timer.stop()
            self.is_recording = False

    def flag(self):
        print("Flag button pressed")

    def update_timer(self):
        self.elapsed_time += 1
        minutes = self.elapsed_time // 60
        seconds = self.elapsed_time % 60
        self.timer_label.setText(f'{minutes:02}:{seconds:02}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SoundRecordingApp()
    sys.exit(app.exec_())
