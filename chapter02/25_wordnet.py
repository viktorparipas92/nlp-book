from nltk.corpus import wordnet as wn

motorcar_first_meaning = wn.synsets('motorcar')[0]

print(motorcar_first_meaning.lemma_names())
# ['car', 'auto', 'automobile', 'machine', 'motorcar'])
print(motorcar_first_meaning.definition())
print(motorcar_first_meaning.examples())

for synset in wn.synsets('car'):
    print(synset.lemma_names())

print(wn.lemmas('car'))


# Find hypernyms and hyponyms of milk
for milk in wn.lemmas('milk'):
    milk_synset = milk.synset()
    print(milk_synset.hypernyms(), milk_synset.hyponyms())


# More lexical relations
# Meronyms and holonyms
wn.synset('tree.n.01').part_meronyms()
# [Synset('burl.n.02'), Synset('crown.n.07'), Synset('stump.n.01'), Synset('trunk.n.01'), Synset('limb.n.02')]
wn.synset('tree.n.01').substance_meronyms()  # [Synset('heartwood.n.01'), Synset('sapwood.n.01')]
wn.synset('tree.n.01').member_holonyms()  # [Synset('forest.n.01')]
wn.synset('mint.n.04').part_holonyms()  # [Synset('mint.n.02')]
wn.synset('mint.n.04').substance_holonyms()  # [Synset('mint.n.05')]

# Entailments
wn.synset('walk.v.01').entailments()  # [Synset('step.v.01')]
wn.synset('eat.v.01').entailments()  # [Synset('swallow.v.01'), Synset('chew.v.01')]
wn.synset('tease.v.03').entailments()  # [Synset('arouse.v.07'), Synset('disappoint.v.01')]

# Antonyms
wn.lemma('supply.n.02.supply').antonyms()  # [Lemma('demand.n.02.demand')]
wn.lemma('rush.v.01.rush').antonyms()  # [Lemma('linger.v.04.linger')]
wn.lemma('horizontal.a.01.horizontal').antonyms()  # [Lemma('vertical.a.01.vertical'), Lemma('inclined.a.02.inclined')]
wn.lemma('staccato.r.01.staccato').antonyms()  # [Lemma('legato.r.01.legato')]


# Semantic similarity
right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')
right.lowest_common_hypernyms(minke)  # [Synset('baleen_whale.n.01')]
right.lowest_common_hypernyms(orca)  # [Synset('whale.n.02')]
right.lowest_common_hypernyms(tortoise)  # [Synset('vertebrate.n.01')]
right.lowest_common_hypernyms(novel)  # [Synset('entity.n.01')]
wn.synset('baleen_whale.n.01').min_depth()  # 14
wn.synset('whale.n.02').min_depth()  # 13
wn.synset('vertebrate.n.01').min_depth()  # 8
wn.synset('entity.n.01').min_depth()  # 0
right.path_similarity(minke)  # 0.250
right.path_similarity(orca)  # 0.167
right.path_similarity(tortoise)  # 0.0769
right.path_similarity(novel)  # 0.0435



