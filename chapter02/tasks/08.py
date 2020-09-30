from nltk.corpus import names
from nltk import ConditionalFreqDist


# Define a conditional frequency distribution over the Names Corpus that allows
# you to see which initial letters are more frequent for males versus females
cfd = ConditionalFreqDist(
    (fileid, name[0]) for fileid in names.fileids() for name in names.words(fileid))
cfd.tabulate()


# Pick a pair of texts and study the differences between them, in terms of vocabulary, vocabulary richness, genre, etc.
# Can you find pairs of words that have quite different meanings across the two texts, such as monstrous in Moby Dick
# and in Sense and Sensibility?
