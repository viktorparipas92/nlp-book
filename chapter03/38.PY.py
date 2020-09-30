import nltk, pprint


def segment(text, segments):
    words = []
    last = 0
    for i in range(len(segments)):
        if segments[i] == '1':
            words.append(text[last:i+1])
            last = i + 1
    words.append(text[last:])
    return words


def evaluate(text, segments):
    words = segment(text, segments)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words))))
    return text_size + lexicon_size


# 3.8 Segmentation

# Sentence segmentation
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sentences = sentence_tokenizer.tokenize(text)
pprint.pprint(sentences[171:181])


# Word segmentation
text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
seg2 = "0100100100100001001001000010100100010010000100010010000"
# Segment with different word boundaries
print(segment(text, seg1))
print(segment(text, seg2))

print(evaluate(text, seg1))
print(evaluate(text, seg2))
