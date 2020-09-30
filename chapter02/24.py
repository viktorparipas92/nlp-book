# LEXICAL RESOURCES
from nltk.corpus import gutenberg, nps_chat, reuters
from nltk.corpus import stopwords, words, names
from nltk import ConditionalFreqDist


# Wordlist corpora
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)


def content_fraction(text):
    content = [w for w in text if w.lower() not in stopwords.words('english')]
    return len(content) / len(text)


print(unusual_words(gutenberg.words('austen-sense.txt')))
# ['abbeyland', 'abhorrence', 'abominably', 'abridgement', 'accordant', 'accustomary',
# 'adieus', 'affability', 'affectedly', 'aggrandizement', 'alighted', 'allenham',
# 'amiably', 'annamaria', 'annuities', 'apologising', 'arbour', 'archness', ...]

print(unusual_words(nps_chat.words()))
# ['aaaaaaaaaaaaaaaaa', 'aaahhhh', 'abou', 'abourted', 'abs', 'ack', 'acros',
# 'actualy', 'adduser', 'addy', 'adoted', 'adreniline', 'ae', 'afe', 'affari', 'afk',
# 'agaibn', 'agurlwithbigguns', 'ahah', 'ahahah', 'ahahh', 'ahahha', 'ahem', 'ahh', ...]


# Stopwords
print(stopwords.words('english'))
# print(content_fraction(reuters.words()))


# Names
print(names.fileids())  # male, female
male_names = names.words('male.txt')
female_names = names.words('female.txt')
print([w for w in male_names if w in female_names])  # unisex names

# Plot names according to last letter (separately for male/female)
cfd = ConditionalFreqDist(
    (fileid, name[-1])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()






