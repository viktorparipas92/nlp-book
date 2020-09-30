# 5. CATEGORIZING AND TAGGING WORDS
# 5.1 Using a tagger
import nltk
from nltk.corpus import brown


def print_word_to_word_phrases(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if t1.startswith('V') and t2 == 'TO' and t3.startswith('V'):
            print(w1, w2, w3)


text = nltk.word_tokenize("And now for something completely different")
print(nltk.pos_tag(text))

text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
print(nltk.pos_tag(text))


# 5.2 Tagged corpora
# Representing tagged tokens
tagged_token = nltk.tag.str2tuple('fly/NN')
print(tagged_token)  # ('fly', 'NN')

# Reading tagged corpora
print(nltk.corpus.brown.tagged_words())
# [('The', 'AT'), ('Fulton', 'NP-TL'), ('County', 'NN-TL'), ...]
print(nltk.corpus.brown.tagged_words(simplify_tags=True))
# [('The', 'DET'), ('Fulton', 'N'), ('County', 'N'), ...]

brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
# brown_news_tagged = brown.tagged_words(categories='news', tagset=)
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
print(tag_fd.keys())
# ['N', 'P', 'DET', 'NP', 'V', 'ADJ', ',', '.', 'CNJ', 'PRO', 'ADV', 'VD', ...]


# Nouns
word_tag_bigrams = nltk.bigrams(brown_news_tagged)
# Word tags occurring most frequently in front of a noun
print(list(nltk.FreqDist(first[1] for (first, second) in word_tag_bigrams if second[1] == 'N')))


# Verbs
wsj = nltk.corpus.treebank.tagged_words(simplify_tags=True)
word_tag_fd = nltk.FreqDist(wsj)
# Most common verbs in news text
print([f"{word}/{tag}" for (word, tag) in word_tag_fd if tag.startswith('V')])

cfd1 = nltk.ConditionalFreqDist(wsj)
print(cfd1['yield'].keys())  # ['V', 'N']
print(cfd1['cut'].keys())  # ['V', 'VD', 'N', 'VN']

cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
# Most frequent past participles
print(cfd2['VN'].keys())  # ['been', 'expected', 'made', ...]

# List of words with same 2nd and 3rd form
print([w for w in cfd1.conditions() if 'VD' in cfd1[w] and 'VN' in cfd1[w]])
['Asked', 'accelerated', 'accepted', 'accused', 'acquired', 'added', 'adopted', ...]
idx1 = wsj.index(('kicked', 'VD'))
print(wsj[idx1-4:idx1+1])
# [('While', 'P'), ('program', 'N'), ('trades', 'N'), ('swiftly', 'ADV'), ('kicked', 'VD')]
idx2 = wsj.index(('kicked', 'VN'))
print(wsj[idx2-4:idx2+1])
# [('head', 'N'), ('of', 'P'), ('state', 'N'), ('has', 'V'), ('kicked', 'VN')]


# Exploring tagged corpora
brown_learned_text = brown.words(categories='learned')
print(sorted(set(second for (first, second) in nltk.bigrams(brown_learned_text) if first == 'often')))
# [',', '.', 'accomplished', 'analytically', ... ]

brown_learned_tagged = brown.tagged_words(categories='learned', simplify_tags=True)
tags = [second[1] for (first, second) in nltk.bigrams(brown_learned_tagged) if first[0] == 'often']
fd = nltk.FreqDist(tags)
print(fd.tabulate())


for tagged_sent in brown.tagged_sents():
    print_word_to_word_phrases(tagged_sent)

brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_news_tagged)

for word in data.conditions():
    if len(data[word]) > 3:
        tags = data[word].keys()
        print(word, ' '.join(tags))



