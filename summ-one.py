import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
# import heapq
# import re
import openai
import dotenv, os
# from gensim.summarization import summarize

dotenv.load_dotenv()
openai.api_key = os.getenv('SECRET_KEY')
# Your input text
with open('dump.txt','r',encoding='utf-8') as inp_file:
    data = inp_file.read()

nltk.download("punkt")
nltk.download("stopwords")

# Tokenize the text into sentences and words
sentences = sent_tokenize(data)
words = word_tokenize(data)

# Remove stopwords and perform stemming
stop_words = set(stopwords.words("english"))
stemmer = nltk.PorterStemmer()
filtered_words = [stemmer.stem(word) for word in words if word.lower() not in stop_words and word.isalnum()]

# Join the filtered words to create a preprocessed version of the text
preprocessed_text = " ".join(filtered_words)


# Summarize the text
# summary = summarize(preprocessed_text, ratio=0.2)
response = openai.Completion.create(
        engine="davinci-codex",  # Choose the GPT-3 engine
        prompt=preprocessed_text,
        temperature=0.5,  # Controls randomness in the output; adjust as needed
        max_tokens=150,  # Set the maximum number of tokens in the generated output
        n=1,  # Number of completions to generate
        stop=None  # You can specify a stopping criterion if needed
    )
summary = response.choices[0].text.strip()

# Print the summary
print(summary)
