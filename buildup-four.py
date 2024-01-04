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


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import sounddevice as sd
import soundfile as sf
import threading

class SoundRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sound Recorder")
        self.root.geometry("400x100")

        # Configure light mode theme
        self.style = ttk.Style()
        self.style.configure("TFrame", background="white")
        self.style.configure("TLabel", background="white", foreground="black")
        self.style.configure("TButton", background="white", foreground="black")
        self.style.configure("TButton.Focus", background="white")
        self.style.map("TButton", background=[("active", "#DDDDDD")])

        self.recording = False
        self.recording_start_time = None

        self.create_widgets()

    def create_widgets(self):
        self.timer_label = ttk.Label(self.root, text="00:00", font=("Helvetica", 30))
        self.timer_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.record_button = ttk.Button(self.root, text="Record", command=self.toggle_recording, style="Record.TButton")
        self.record_button.grid(row=1, column=1, pady=20, padx=10)

        self.pause_button = ttk.Button(self.root, text="Pause", command=self.pause_recording, style="Small.TButton")
        self.pause_button.grid(row=1, column=0, pady=20, padx=10)

        self.flags_button = ttk.Button(self.root, text="Flags", command=self.flag_recording, style="Small.TButton")
        self.flags_button.grid(row=1, column=2, pady=20, padx=10)

    def toggle_recording(self):
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.recording = True
        self.recording_start_time = datetime.now()
        self.record_button["text"] = "Stop"

        # Start recording in a separate thread
        self.recording_thread = threading.Thread(target=self.record_audio)
        self.recording_thread.start()

    def stop_recording(self):
        self.recording = False
        self.record_button["text"] = "Record"
        
        # Wait for the recording thread to finish
        self.recording_thread.join()

    def pause_recording(self):
        # Add functionality for pause button (if needed)
        pass

    def flag_recording(self):
        # Add functionality for flags button (if needed)
        pass

    def record_audio(self):
        try:
            with sf.SoundFile("recorded_audio.wav", mode='x', samplerate=44100, channels=1) as file:
                def callback(indata, frames, time, status):
                    if status:
                        print(status)
                    if self.recording:
                        file.write(indata)

                # Record audio using sounddevice
                with sd.InputStream(callback=callback):
                    self.root.after(1000, self.update_timer)  # Schedule timer update after 1 second
                    self.root.mainloop()  # Start the Tkinter main loop

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.recording = False
            self.record_button["text"] = "Record"

    def update_timer(self):
        if self.recording_start_time and self.recording:
            elapsed_time = datetime.now() - self.recording_start_time
            formatted_time = "{:02}:{:02}".format(elapsed_time.seconds // 60, elapsed_time.seconds % 60)
            self.timer_label["text"] = formatted_time
            self.root.after(1000, self.update_timer)  # Schedule the next update after 1 second

if __name__ == '__main__':
    root = tk.Tk()

    # Define styles for buttons
    root.style = ttk.Style()
    root.style.configure("Record.TButton", font=("Helvetica", 16), width=15)
    root.style.configure("Small.TButton", font=("Helvetica", 12), width=8)

    app = SoundRecorderApp(root)
    root.mainloop()
