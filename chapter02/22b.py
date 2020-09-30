from nltk.corpus import genesis
from nltk import bigrams, ConditionalFreqDist


def generate_model(cfdist, start_word, num=15):
    word = start_word
    for i in range(num):
        yield word
        word = cfdist[word].max()  # Takes most frequent word after each one


text = genesis.words('english-kjv.txt')
bigrams = bigrams(text)
cfd = ConditionalFreqDist(bigrams)

print(cfd['living'])
for w in generate_model(cfd, 'ye'):
    print(w)
