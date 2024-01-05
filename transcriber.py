
import whisper

class Transcriber:
    
    def transcribe(audio : str):
        
        # load the audio 
        loaded_audio = whisper.load_audio(audio)
        
        # create the transcription model 
        model = whisper.load_model("base")
        # initiate transcription of the audio chunk
        transcription = whisper.transcribe(audio=loaded_audio , model=model , fp16 = False , task = "translate" , language = "en" )
        print(transcription["text"])
        # # append that to dump.txt 
        file = open(file= "dump.txt" , mode='a')
        file.write(transcription["text"])
        file.close()
        
# Transcriber.transcribe("output.wav")