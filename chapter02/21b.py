from nltk.corpus import cess_esp, floresta, udhr
# from nltk.corpus import indian
from nltk import ConditionalFreqDist


# Corpora in other languages
print(cess_esp.words())
print(floresta.words())
# print(indian.words('hindi.pos'))

print(udhr.fileids())
print(udhr.words('Javanese-Latin1')[11:])
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = ConditionalFreqDist((lang, len(word)) for lang in languages for word in udhr.words(f"{lang}-Latin1"))
cfd.plot(cumulative=True)

