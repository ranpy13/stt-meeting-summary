import threading
import recorder
# import transcriber

class Converter:
    def saveAudio(self, tm, fn):
        recorder.record(self, tm, fn)

    def transcriber(self):
        # trasncriber text here
        pass
    
    def convert(self):
        while True:
            ps = 1 # first pass and subsequents
            rec = threading.Thread(target=self.saveAudio, args=[60,f"sch{ps}.wav"])
            tsc = threading.Thread(target=self.transcriber, args=())
            ps += 1

            rec.start()
            tsc.start()

            rec.join()
            tsc.join()



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon, QFont, QMovie
from PyQt5.QtCore import QTimer, QTime, Qt

class SoundRecorderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.recording = False
        self.recording_start_time = None
        self.setFixedSize(400, 500)
        self.conv = Converter()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Sound Recorder')
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #202939")

        # Timer Label
        self.timer_label = QLabel('00:00', self)
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setFont(QFont('Helvetica', 30))
        self.timer_label.setStyleSheet("color: white")

        # Waveform Label
        self.wvfrm_label = QLabel(self)
        self.wvfrm_label.setGeometry(50, 100, 300, 150)
        self.waveform = QMovie("waveform.gif")
        self.wvfrm_label.setMovie(self.waveform)
        self.wvfrm_label.setStyleSheet("background-color: white")
        self.waveform.start()
        self.waveform.stop()

        # Play, Pause, Flag Buttons
        # self.play_button = self.create_button('ply.png', self.play_recording)
        self.pause_button = self.create_button('pau.png', self.pause_recording, small=True)
        self.flag_button = self.create_button('flg.png', self.flag_recording, small=True)
        self.record_button = self.create_button('rec.png', self.toggle_recording, large=True)

        # Horizontal Layout
        hbox1 = QHBoxLayout()
        # hbox.addWidget(self.play_button)
        hbox1.addWidget(self.pause_button)
        hbox1.addWidget(self.record_button)
        hbox1.addWidget(self.flag_button)

        # Vertical Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.timer_label)
        vbox.addSpacing(250)
        vbox.addLayout(hbox1)
        # vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.setLayout(vbox)

        # Timer Update
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

    def create_button(self, icon_filename, slot_function, small=False, large=False):
        button = QPushButton(self)
        button.setIcon(self.create_icon(icon_filename))
        button.setGeometry(200, 150, 100, 30)
        button.setFixedSize(100, 100)
        # button.setStyleSheet("border-radius: 1")
        button.clicked.connect(slot_function)
        
        if small:
            button.setFixedSize(70, 70)
            button.setStyleSheet("background-color: #FDFD96; border-radius : 35; border : 2px solid black")
            # button.setStyleSheet('border-radius: 25px;')
        elif large:
            button.setFixedSize(120, 120)
            button.setStyleSheet("background-color: #FF6961; border-radius : 60; border : 2px solid black")
            # button.setStyleSheet("border-radius : 50; border : 2px solid black")
            # button.setStyleSheet('border-radius: 40px;')
        else:
            button.setFixedSize(70, 70)
            button.setStyleSheet("background-color: #FDFD96")
            # button.setStyleSheet('border-radius: 35px;')

        return button

    def create_icon(self, filename):
        pixmap = QPixmap(filename)
        icon = QIcon(pixmap)
        return icon

    def toggle_recording(self):
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.recording = True
        self.recording_start_time = QTime.currentTime()
        self.waveform.start()
        self.conv.convert()
        self.timer_label.setStyleSheet('color: #C9DFC8;')
        self.timer_label.setFont(QFont('Helvetica', 30, QFont.Bold))
        self.timer.start(1000)  # Timer interval: 1000 ms (1 second)

        # Add logic to start recording

    def stop_recording(self):
        self.recording = False
        self.timer.stop()
        self.waveform.stop()
        
        self.timer_label.setStyleSheet('color: #77DDFF;')
        self.timer_label.setFont(QFont('Helvetica', 30))
        # Add logic to stop recording

    def pause_recording(self):
        # Add functionality for pause button (if needed)
        pass

    def play_recording(self):
        # Add functionality for play button (if needed)
        pass

    def flag_recording(self):
        # Add functionality for flag button (if needed)
        pass

    def update_timer(self):
        elapsed_time = self.recording_start_time.elapsed()
        formatted_time = "{:02}:{:02}".format(elapsed_time // 60000, (elapsed_time // 1000) % 60)
        self.timer_label.setText(formatted_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    recorder_app = SoundRecorderApp()
    recorder_app.show()
    sys.exit(app.exec_())
