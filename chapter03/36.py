import nltk


# 3.6 Normalizing text
raw = """
DENNIS: Listen, strange women lying in ponds distributing swords
is no basis for a system of government. Supreme executive power derives from
a mandate from the masses, not from some farcical aquatic ceremony.
"""
tokens = nltk.word_tokenize(raw)


# Stemmers
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
print([porter.stem(t) for t in tokens])
print([lancaster.stem(t) for t in tokens])


# Lemmatization (slower but more precise)
lemmatizer = nltk.WordNetLemmatizer()
print([lemmatizer.lemmatize(t) for t in tokens])
