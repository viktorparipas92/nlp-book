from nltk.corpus import brown, inaugural, udhr
from nltk import ConditionalFreqDist, bigrams
# Conditional Frequency Distributions


# Counting words by genre
cfd = ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
# Only two genres
genre_word = [(genre, word) for genre in ['news', 'romance'] for word in brown.words(categories=genre)]
print(len(genre_word))  # number of genre-word pairs
cfd_two_genres = ConditionalFreqDist(genre_word)
print(cfd_two_genres.conditions())  # news, romance
print(cfd['news'])
print(cfd['romance'])
print(list(cfd['romance']))
print(cfd['romance']['could'])


# Plotting and tabulating distributions
cfd = ConditionalFreqDist(
    (target, fileid[:4]) for fileid in inaugural.fileids()
    for w in inaugural.words(fileid) for target in ['america', 'citizen'] if w.lower().startswith(target))

languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = ConditionalFreqDist(
    (lang, len(word)) for lang in languages for word in udhr.words(f"{lang}-Latin1"))
cfd.tabulate(conditions=['English', 'German_Deutsch'], samples=range(10), cumulative=True)


# Generating random text with bigrams
sentence_string = 'In the beginning God created the heaven and the earth .'
sentence = sentence_string.split(' ')
for b in bigrams(sentence):
    print(b)





