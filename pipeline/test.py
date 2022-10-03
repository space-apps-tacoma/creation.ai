from preprocessing import extract_text
from analysis import wordcloud, frequency_distribution
from summariser import summarizer

import matplotlib.pyplot as plt

text = extract_text('./data/19810002941.pdf')


wordcloud = wordcloud(text)

fig = plt.figure(
    figsize = (40, 30),
    facecolor = 'k',
    edgecolor = 'k'
)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()


fig = frequency_distribution(text)
fig.show()

summary = summarizer(text)
print(summary)
