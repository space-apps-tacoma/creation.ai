from preprocessing import basic_preprocessing, preprocess_frequencies
import PyPDF2
import re
import nltk
import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from english_words import english_words_set
from nltk.probability import FreqDist
from tqdm import tqdm
import plotly.express as px

def wordcloud(text=str):

    cleaned_content = basic_preprocessing(text)

    wordcloud = WordCloud(
        width = 1500,
        height = 750,
        background_color = 'black',
        max_words=150,
        min_word_length=4,
        stopwords = STOPWORDS
    ).generate(cleaned_content)

    return wordcloud

def frequency_distribution(text=str):
    
    n_text = preprocess_frequencies(text).split()
            
    fdist = FreqDist(n_text)
    
    imp_words_freqs = fdist.most_common(40)

    imp_words = []
    freqs = []

    for i in imp_words_freqs:
        imp_words.append(i[0])
        freqs.append(i[1])

    fig = px.bar(x = imp_words, y = freqs,color = freqs, labels=dict(x="Words", y="Frequencies"))
    fig.update_xaxes(tickangle=45)
    fig.update_layout(title_text ='Bar Graph indicating the most occuring words in the document along with their frequencies',title_x=0.5,title_y=0.99)
    
    return fig
