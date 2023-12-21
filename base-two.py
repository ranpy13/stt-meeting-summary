from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
import json
import subprocess
from transformers import pipeline
import pyaudio
import ipywidgets as widgets
from IPython.display import display

FRAME_RATE = 16000
CHANNELS=1

model = Model(model_name="vosk-model-en-us-0.22")
# For a smaller download size, use model = Model(model_name="vosk-model-small-en-us-0.15")
rec = KaldiRecognizer(model, FRAME_RATE)
rec.SetWords(True)

mp3 = AudioSegment.from_mp3("marketplace.mp3")
mp3 = mp3.set_channels(CHANNELS)
mp3 = mp3.set_frame_rate(FRAME_RATE)
rec.AcceptWaveform(mp3.raw_data)
result = rec.Result()

text = json.loads(result)["text"]
cased = subprocess.check_output('python recasepunc/recasepunc.py predict recasepunc/checkpoint', shell=True, text=True, input=text)

def voice_recognition(filename):
    model = Model(model_name="vosk-model-en-us-0.22")
    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)
    
    mp3 = AudioSegment.from_mp3(filename)
    mp3 = mp3.set_channels(CHANNELS)
    mp3 = mp3.set_frame_rate(FRAME_RATE)
    
    step = 45000
    transcript = ""
    for i in range(0, len(mp3), step):
        print(f"Progress: {i/len(mp3)}")
        segment = mp3[i:i+step]
        rec.AcceptWaveform(segment.raw_data)
        result = rec.Result()
        text = json.loads(result)["text"]
        transcript += text
    
    cased = subprocess.check_output('python recasepunc/recasepunc.py predict recasepunc/checkpoint', shell=True, text=True, input=transcript)
    return cased

transcript = voice_recognition("sample_audio.mp3")
summarizer = pipeline("summarization")
# For a smaller model, use: summarizer = pipeline("summarization", model="t5-small")
split_tokens = transcript.split(" ")
docs = []
for i in range(0, len(split_tokens), 850):
    selection = " ".join(split_tokens[i:(i+850)])
    docs.append(selection)

summaries = summarizer(docs)
summary = "\n\n".join([d["summary_text"] for d in summaries])
print(summary)

def record_microphone(seconds=10, chunk=1024, audio_format=pyaudio.paInt16):
    p = pyaudio.PyAudio()

    stream = p.open(format=audio_format,
                    channels=CHANNELS,
                    rate=FRAME_RATE,
                    input=True,
                    input_device_index=2,
                    frames_per_buffer=chunk)

    frames = []

    for i in range(0, int(FRAME_RATE / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    sound = AudioSegment(
        data=b''.join(frames),
        sample_width=p.get_sample_size(audio_format),
        frame_rate=FRAME_RATE,
        channels=CHANNELS
    )
    sound.export("temp.mp3", "mp3")
    
record_microphone()

# GUI
record_button = widgets.Button(
    description='Record',
    disabled=False,
    button_style='success',
    tooltip='Record',
    icon='microphone'
)

summary = widgets.Output()

def start_recording(data):
    with summary:
        display("Starting the recording.")
        record_microphone()
        display("Finished recording.")
        transcript = voice_recognition("temp.mp3")
        display(f"Transcript: {transcript}")

record_button.on_click(start_recording)

display(record_button, summary)