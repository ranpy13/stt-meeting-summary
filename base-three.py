from openai import OpenAI
import dotenv, os

dotenv.load_dotenv()
api_key = os.getenv('SECRET_KEY')

client = OpenAI(api_key=api_key)

audio_file= open("sample2.wav", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  response_format="text"
)

print(transcript)