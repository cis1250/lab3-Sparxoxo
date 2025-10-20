#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re
import string


def is_sentence(text):

    if not isinstance(text, str) or not text.strip():
        return False


    if not text[0].isupper():
        return False


    if not re.search(r'[.!?]$', text):
        return False


    if not re.search(r'\w+', text):
        return False

    return True


user_sentence = input("Enter a sentence: ")
while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

tokens = user_sentence.split()
words = []
freqs = []
for token in tokens:
    word = token.strip(string.punctuation).lower()  
    if word == "":
        continue
    if word in words:
        i = words.index(word)
        freqs[i] += 1
    else:
        words.append(word)
        freqs.append(1)
for i in range(len(words)):
   print(words[i] + ":", freqs[i])

