import nltk, re


# 3.7 Regular expressions for tokenizing text
# Simple approaches to tokenization
raw = """'
When I'M a Duchess,' she said to herself, (not in a very hopeful tone
though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
well without--Maybe it's always pepper that makes people hot-tempered,'...
"""

# Splitting
# print(re.split(r' ', raw))  # split on space
# print(re.split(r'[ \t\n]+', raw))  # split on any whitespace
# print(re.split(r'\W+', raw))  # split on any non-alphanumeric characters
# print(re.findall(r'\w+|\S\w*', raw))
# print(re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw))  # this works pretty well


# NLTK's regex tokenizer
text = 'That U.S.A. poster-print costs $12.40...'
pattern = r'''(?x)([A-Z]\.)+|\w+(-\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_`]'''  # NOT WORKING!!!
print(nltk.regexp_tokenize(text, pattern))
# ['That', 'U.S.A.', 'poster-print', 'costs', '$12.40', '...']
