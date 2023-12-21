from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize(text, language="english", sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    # return ' '.join([str(sentence) for sentence in summary])
    return [str(sentence) for sentence in summary]

if __name__ == "__main__":
    with open('dump.txt','r',encoding='utf-8') as inp_file:
        data = inp_file.read()
    text = data
    count = max(text.count(' ')//100, 5)
    summary = summarize(text, sentences_count=count)
    # print(summary)
    print("Generating Summary... ", end="")
    with open('summary.txt','w') as res:
        for points in summary:
            res.write("-\t"+points+"\n")
        res.close()
    print("Generated!")
