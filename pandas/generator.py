import pandas as pd
file_path = '/home/nli31/github/python-learning/pandas/words.txt'


def value_str(s: str)-> int:
    return sum([ ord(c)-96 for c in s])

file = open(file_path, 'r')
lines = file.readlines()

column_headers = [
    'Word',
    'Char Count',
    'Value'
]
words = []
print(words)
print(type(words))
# Word, Char Count,	Value	
for word in lines:
    word = word.strip()
    words.append([word, len(word), value_str(word)])

f = pd.DataFrame(words, columns=column_headers)
print(f)

f.to_csv(f'./words.csv', index=False)
    