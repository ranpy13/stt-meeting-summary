# Speech to Text | Meeting summarizer model
---
## Description
* The goal is to make a model which **translates audio from meetings and encodes it to a text file**, which on completion is *summarized* in to a smaller, concise *list of bullet points* covering the entire meeting. The initial idea is to implement it through pre-trained models, but the accuracy and efficiency has to take care of.
* There are a few considersation. First, that it should desirably also support *mulit-lingual conversation*, with **english** being the primary support, and additional support for **hindi** and at least the default regional language.
* The end goal however, is to wrap this model into a presentable *web-app*, with gui interface to start the recording, and add the administrators to the meetings, which will *recieve the summary as a text file in the mail box* automatically, without manual intervention.

## Problem Statement
> `To create a machine learning model which can listen to the audio from meetings and translate the speech to text, and finally output a summary of the entire meeting in a text format. This model can further be wrapped inside a graphical interface for easier access, where the summarized text has to be sent to the administrators of the meeting provided on onset.`

## Course of Action
### Setting the baseline
* using google's standard api to convert speech to text[^1]
  * setting a baseline 
  * finding accuracy
  * improving on the same
* dumping the output to a text file
  * that is then picked up for summarizing
  * using ~~genism~~[^2] [^3] *sumy* standard module[^4] [^5]
  * improving on the same

### Improving on the baseline
* having got the baseline in 
  * google's `speechrecognition`[^6] for converting speech to text
  * `sumy-lsasummarize`[^7] for summarizing the contents
* to use them together and streamline the model
  * bridge the gap between the two - **preprocessing**
  * *process* the output from converted text with proper punctuation and markings
  * then running the summarizing models on the processed text block
* thus, require a middleware leveragin a *natural languge processing* model
  * current options - `nltk`[^8], `openai`[^9], `spacy`[^10]
* _**major shift** in workflow_, found better option: [^11]
  * **`vosk` model** for speech to text convertion
  * preprocessing through **`transforerms` model**
  * finally, summarizing through _`pipeline()`_

### Advanced Optimization and Improvization
* Context aware summary
  * change of paragraph in cases of change of paragraph
  * might require deep learning,
  * can seperate two summaries, general and context based summary
* Multilingual speech optimization
* Adapting to bandwidth, backup solutions
  * recording set audio 
  * fall-back to recording and translating the saved audio instead of live time transcribing

\
\
&nbsp;&nbsp;&nbsp;&nbsp;
---
## References & Bibliography
[^1]: GfG articles on speech-to-text [Python: Con...](https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/)

[^2]: Knowledge Base/ [turing.com](https://www.turing.com/kb/5-powerful-text-summarization-techniques-in-python)

[^3]: Developer's documentation for [`genism`](https://radimrehurek.com/gensim/)

[^4]: Sasha Bondar's blog post on [reintech.io](https://reintech.io/blog/how-to-create-a-text-summarization-tool-with-sumy-tutorial-for-developers)

[^5]: Official PyPi documentation for [`sumy`](https://pypi.org/project/sumy/) 

[^6]: Official PyPi documentation for [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/)

[^7]: Official PyPi documentation for [`sumy`](https://pypi.org/project/sumy/)

[^8]: Official PyPi documentation for [`nltk`](https://pypi.org/project/nltk/)

[^9]: Official PyPi documentation for [`openai`](https://pypi.org/project/openai/)

[^10]: Official PyPi documentation for [`spacy`](https://pypi.org/project/spacy/)

[^11]: DataQuest's blog post, [github](https://github.com/dataquestio/project-walkthroughs/blob/master/speech_recognition/README.md)