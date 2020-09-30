from nltk.book import FreqDist, text1, bigrams

# Frequency distributions
fdist1 = FreqDist(text1)
print(fdist1)
fdist1.plot(50, cumulative=True)
print(fdist1.hapaxes())

# Fine-grained selection of words
print(sorted([w for w in set(text1) if len(w) > 10 and fdist1[w] > 3]))

# Collocations and bigrams
bgrms = bigrams(['more', 'is', 'said', 'than', 'done'])
print(text1.collocations())

# Counting other things
length_frequencies = FreqDist([len(w) for w in text1])
print(length_frequencies.keys())
print(length_frequencies.freq(3))
