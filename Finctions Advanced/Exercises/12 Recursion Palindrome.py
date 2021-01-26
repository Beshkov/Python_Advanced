"""
Write a recursive function called palindrome which will receive a word and an index (always 0). \
Implement the function, so it returns "{word} is a palindrome" \
if the word is a palindrome and "{word} is not a palindrome" \
if the word is not a palindrome using recursion. Submit only the function in the judge system.
"""
from math import floor
def palindrome(word, ind=0):


    if floor(len(word)/2) == ind:
        return f'{word} is a palindrome'


    if word[ind] == word[-(1+ind)]:
        return palindrome(word, ind+1)

    else:
        return f'{word} is not a palindrome'

print(palindrome('abcza'))
