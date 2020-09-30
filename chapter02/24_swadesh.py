from nltk.corpus import swadesh


print(swadesh.fileids())  # be, bg, bs, ca...
print(swadesh.words('en'))


fr2en = swadesh.entries(['fr', 'en'])
# [('je', 'I'), ('tu, vous', 'you (singular), thou'), ('il', 'he'), ...]
translate = dict(fr2en)
print(translate['chien'])  # dog
print(translate['jeter'])  # throw
