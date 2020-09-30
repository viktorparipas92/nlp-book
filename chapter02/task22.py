from nltk.corpus import brown
from nltk import ConditionalFreqDist

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
categories = ['news', 'romance']

cfd = ConditionalFreqDist(
    (day, category)
    for category in categories
    for word in brown.words(categories=category)
    for day in days
    if word.lower().startswith(day.lower()))

cfd.tabulate()
