import PyPDF2
import re
import nltk
import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from english_words import english_words_set
from nltk.probability import FreqDist
from tqdm import tqdm

def extract_text(filepath):

    content = ""

    pdfFile = open(filepath, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)

    for i in range(pdfReader.numPages):
        pg_content = pdfReader.getPage(i)
        content += pg_content.extractText()

    content = re.sub('\n', ' . ', content)

    return content

def basic_preprocessing(content):

    stemmer = nltk.stem.WordNetLemmatizer()
    text = nltk.tokenize.word_tokenize(content)
    stopwords = nltk.corpus.stopwords.words("english")
    n_text = []

    for word in text:
        word = word.lower()
        if word not in string.punctuation and word.isalnum() and not word.isdigit():
            word = re.sub('\n', '.', word)
            word = re.sub('\t', '.', word)
            word = re.sub(r'\$\w*', '', word)
            word = re.sub('[^a-zA-Z]',' ',word)
            word = stemmer.lemmatize(word)
            n_text.append(word)

    cleaned_content = ' '.join(n_text)

    return cleaned_content

def preprocess_frequencies(content):

    stemmer = nltk.stem.WordNetLemmatizer()
    text = nltk.tokenize.word_tokenize(content)
    stopwords = nltk.corpus.stopwords.words("english")
    extra_stopwords = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.',',']
    stopwords.extend(extra_stopwords)
    spec_char = ' !@#$%^&*()_+{}|:M<>?>,./;][=-\1234567890'
    
    correct_words = english_words_set
    
    n_text = []
    
    for word in text:
        word = word.lower()
        if word not in stopwords and word not in spec_char and word not in string.punctuation and word.isalnum() and not word.isdigit():

            word = re.sub('\n', '', word)
            word = re.sub('\t', '', word)
            word = re.sub(r'\$\w*', '', word)

            word = stemmer.lemmatize(word)
            n_text.append(word)
    
    cleaned_content = ' '.join(n_text)
            
    return cleaned_content
