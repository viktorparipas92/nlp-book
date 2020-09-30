from nltk import FreqDist, ConditionalFreqDist
from nltk.corpus import gutenberg
from nltk.corpus import webtext
from nltk.corpus import nps_chat
from nltk.corpus import brown
from nltk.corpus import reuters
from nltk.corpus import inaugural

# Accessing text corpora
emma = gutenberg.words('austen-emma.txt')
# emma = nltk.Text(gutenberg.words('austen-emma.txt'))
# emma.concordance('some')
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print(int(num_chars / num_words), int(num_words / num_sents), int(num_words / num_vocab), fileid)


# Web and chat text
for fileid in webtext.fileids():
    print(fileid, f"{webtext.raw(fileid)[:65]}...")

chatroom = nps_chat.posts('10-19-20s_706posts.xml')
print(chatroom[123])


# Brown corpus
print(brown.categories())
print(brown.words(categories='news'))
print(brown.words(fileids=['cg22']))
print(brown.sents(categories=['news', 'editorial', 'reviews']))

news_text = brown.words(categories='news')
fdist = FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(f"{m}: {fdist[m]}")

cfd = ConditionalFreqDist(
    (genre, word) for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
cfd.tabulate(conditions=genres, samples=modals)


# Reuters corpus
print(reuters.fileids())
print(reuters.categories())
print(reuters.categories('training/9865'))
print(reuters.categories(['training/9865', 'training/9880']))
print(reuters.fileids('barley'))
print(reuters.fileids(['barley', 'corn']))

print(reuters.words('training/9865')[:14])
print(reuters.words(['training/9865', 'training/9880']))
print(reuters.words(categories='barley'))
print(reuters.words(categories=['barley', 'corn']))


# Inaugural addresses
print(inaugural.fileids())
print([fileid[:4] for fileid in inaugural.fileids()])  # years of addresses
cfd = ConditionalFreqDist(
    (target, fileid[:4]) for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))
cfd.plot()




