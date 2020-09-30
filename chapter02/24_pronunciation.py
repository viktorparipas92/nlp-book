from nltk.corpus import cmudict
from nltk import ConditionalFreqDist


# A pronouncing dictionary
entries = cmudict.entries()
print(len(entries))

for word, pronunciation in entries:
    if len(pronunciation) == 3:
        ph1, ph2, ph3 = pronunciation
        if ph1 == 'P' and ph3 == 'T':
            print(word, ph2)

syllable = ['N', 'IH0', 'K', 'S']  # nix
print([word for word, pron in entries if pron[-4:] == syllable])
# ["atlantic's", 'audiotronics', 'avionics', 'beatniks', 'calisthenics', 'centronics',
# 'chetniks', "clinic's", 'clinics', 'conics', 'cynics', 'diasonics', "dominic's",
# 'ebonics', 'electronics', "electronics'", 'endotronics', "endotronics'", 'enix', ...]

print([word for word, pron in entries if pron[-1] == 'M' and word[-1] == 'n'])  # ends in n, pronounced m
# ['autumn', 'column', 'condemn', 'damn', 'goddamn', 'hymn', 'solemn']
# Diphthongs at the start of the word pronounced n
print(sorted(set(word[:2] for word, pron in entries if pron[0] == 'N' and word[0] != 'n')))
# ['gn', 'kn', 'mn', 'pn']


# Stress
def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]

print([w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']])
# ['abbreviated', 'abbreviating', 'accelerated', 'accelerating', 'accelerator',
# 'accentuated', 'accentuating', 'accommodated', 'accommodating', 'accommodative',
# 'accumulated', 'accumulating', 'accumulative', 'accumulator', 'accumulators', ...]

print([w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']])
# ['abbreviation', 'abbreviations', 'abomination', 'abortifacient', 'abortifacients',
# 'academicians', 'accommodation', 'accommodations', 'accreditation', 'accreditations',
# 'accumulation', 'accumulations', 'acetylcholine', 'acetylcholine', 'adjudication', ...]


# Get all words which begin with P sound and have three phonemes
# Sorted by the third sound
p3_words = [
    (f"{pron[0]}-{pron[2]}", word)
    for word, pron in entries
    if pron[0] == 'P' and len(pron) == 3]
cfd = ConditionalFreqDist(p3_words)
for template in cfd.conditions():
    if len(cfd[template]) > 10:  # display only those which occur at least 10 times
        words = cfd[template].keys()
        word_list = ' '.join(words)
        print(template, f"{word_list[:70]}...")


prondict = cmudict.dict()
print(prondict['fire'])
# [['F', 'AY1', 'ER0'], ['F', 'AY1', 'R']]


