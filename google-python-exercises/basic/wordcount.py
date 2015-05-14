#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.
"""

def make_list(filename):
    # read the file
    in_file = open(filename, 'rU')
    # turn it into a single string
    text = in_file.read()
    # make the string all lowercase
    low_case = text.lower()
    # turn each word of the string into an element in a list
    word_list = low_case.split()
    return word_list
    
def make_dict(filename):
    # run my make list function to get a list of lowercase strings
    word_list = make_list(filename)
    # create an empty dictionary to populate
    word_dict = {}
    # loop through each word
    for word in word_list:
        # add to the word count if word already exists
        if word in word_dict.keys():
            word_count=word_dict[word]
            word_dict[word]=word_count+1
        # add the word to the dictionary if it does not
        else:
            word_dict[word]=1
        
    return word_dict

def print_words(filename):
    # generate a dictionary containing all the words and counts
    result = make_dict(filename)
    # sort based on the words alphabetically
    sorted_dict = sorted(result.keys())
    # print each word and it's count
    for each_word in sorted_dict:
        print each_word, result[each_word] 
    
def get_count(in_tuple):
    return in_tuple[1]

def print_top(filename):
    # generate a dictionary containing all the words and counts
    result = make_dict(filename)
    # turn each key-value pair into a tuple
    tuple_dir = result.items()
    # sort the tuple by the second item
    sorted_dict = sorted(tuple_dir, key=get_count, reverse = True)
    
    #print the top 25 words
    for each_word in sorted_dict[:25]:
        print each_word[0], each_word[1]
        
"""
    

    
1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
