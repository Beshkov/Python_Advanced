import re

letter_path = r'[a-z]'
punctuation_path = r"[',\.\!\?:;\"\-]"

def get_n(line, path):
    return len(re.findall(path,line,re.IGNORECASE))

with open('text.txt', 'r') as file:
    lines = file.readlines()
    counter = 1
    for line in lines:
        n_letter = get_n(line, letter_path)
        n_punct = get_n(line, punctuation_path)
        print(f'Line {counter}: {line[:-1]} ({n_letter})({n_punct})')