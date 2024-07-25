import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
import heapq
    
def tokenize_sentences(article_text):
    sentence_list = sent_tokenize(article_text)
    return sentence_list

def calculate_frequency(formatted_article_text):
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    maximum_frequncy = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    return word_frequencies

def calculate_scores(sentence_list,word_frequencies):
    sentence_scores = {}
    for sent in sentence_list:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    return sentence_scores


def summarize(text):
    frequency=calculate_frequency(text)
    sentences=tokenize_sentences(text)
    sentence_scores=calculate_scores(sentences,frequency)
    summary_sentences = heapq.nlargest(10, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)    
    return summary

