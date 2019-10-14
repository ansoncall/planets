#! usr/bin/env python3

# This script takes a user-inputted sentence, removes the spaces, changes all chars to lowercase, and counts the number of chars.

# Get user input, change to lowercase, remove spaces
sentence = input('Please enter a sentence: ').lower().replace(' ','')

# Count chars and return
print('The number of characters (excluding spaces) in the sentence is ', len(sentence))
