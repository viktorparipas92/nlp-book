# 3.3 Text processing with Unicode

import nltk
import codecs


# Extracting encoded text from files
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = codecs.open(path, encoding='latin2')

for line in f:
    line = line.strip()
    # print(line.encode('unicode_escape'))  # this prints the Unicode sequences for non-ASCII characters
    print(line)

n_acute = u'\u0144'
print(n_acute)  # ń
print(n_acute.encode('utf8'))  # '\xc5\x84'






