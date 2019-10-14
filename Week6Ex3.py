#! usr/bin/env python3

# This script takes a user-inputted sentence, removes the spaces, changes all chars to lowercase, and counts the number of chars.

# Get user input
sentence = input('Please enter a sentence: ')

# Remove spaces
nospace = replace(sentence, ' ', '')

# Count chars and return
print('The number of characters (excluding spaces) in the sentence is ', nospace.length())
