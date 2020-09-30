# 5.4 Automatic tagging
import nltk
from nltk.corpus import brown


brown_tagged_sentences = brown.tagged_sents(categories='news')
brown_sentences = brown.sents(categories='news')

# The default tagger
tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
print(nltk.FreqDist(tags).max())

#Tag everything as NN
raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
# print(default_tagger.tag(tokens))
# It performs poorly
print(default_tagger.evaluate((brown_tagged_sentences)))


# Regular expression tagger
patterns = [
    (r'.*ing$', 'VBG'), # gerunds
    (r'.*ed$', 'VBD'), # simple past
    (r'.*es$', 'VBZ'), # 3rd singular present
    (r'.*ould$', 'MD'), # modals
    (r'.*\'s$', 'NN$'), # possessive nouns
    (r'.*s$', 'NNS'), # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
    (r'.*', 'NN')  # nouns (default)
]
regexp_tagger = nltk.RegexpTagger(patterns)
print(regexp_tagger.evaluate(brown_tagged_sentences))


# Lookup tagger
fd = nltk.FreqDist(brown.words(categories='news'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
print(fd, cfd)

most_freq_words = fd.most_common()[:100]
likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
baseline_tagger = nltk.UnigramTagger(model=likely_tags)
# Better performance
print(baseline_tagger.evaluate(brown_tagged_sents))
