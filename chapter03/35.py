import nltk
import re
from nltk.corpus import gutenberg, nps_chat, brown


def compress(word):
    regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
    pieces = re.findall(regexp, word)
    return ''.join(pieces)


# 3.5 Useful applications of regular expressions
words_treebank = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vowel_sequence for word in words_treebank for vowel_sequence in re.findall(r'[aeiou]{2,}', word))

english_udhr = nltk.corpus.udhr.words('English-Latin1')
compressed_words = [compress(word) for word in english_udhr[:75]]
print(nltk.tokenwrap(compressed_words))

rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [consonant_and_vowel for word in rotokas_words for consonant_and_vowel in re.findall(r'[ptksvr][aeiou]', word)]
# equivalent to (consonant_and_vowel[0], consonant_and_vowel[1]) ...
cfd = nltk.ConditionalFreqDist(cvs)
cfd.tabulate()

cv_word_pairs = [
    (consonant_and_vowel, word) for word in rotokas_words
    for consonant_and_vowel in re.findall(r'[ptksvr][aeiou]', word)]
cv_index = nltk.Index(cv_word_pairs)
print(cv_index['su'])  # ['kasuari']
print(cv_index['po'])  # ['kaapo', 'kaapopato', 'kaipori', ...]


# Searching tokenized text
# <> is the token boundary
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
moby.findall(r"<a> (<.*>) <man>")  # finds all adjectives for a ... man

chat = nltk.Text(nps_chat.words())
chat.findall(r"<.*> <.*> <bro>")  # you rule bro; telling you bro; u twizted bro

hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
hobbies_learned.findall(r"<\w*> <and> <other> <\w*s>")
# speed and other activities; water and other liquids; tomb and other landmarks...
