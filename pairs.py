#!/usr/bin/env python
"""
How many perfect anagrams are there? (only two words which anagram to each other)
"""

import sys

ANAGRAMS = {}

def load_dictionary(fname):
    f = open(fname)
    for word in f.readlines():
        word = word.rstrip("\n")
        key = "".join(sorted(word))
        if not ANAGRAMS.has_key(key):
            ANAGRAMS[key] = []
        ANAGRAMS[key].append(word)
    f.close()

def main():
    load_dictionary("./dictionary.txt")

    words = [entry[1] for entry in ANAGRAMS.items() if len(entry[1]) == 2] 
    words = sorted(words, key=lambda pair: pair[0])

    for pair in words:
        print ", ".join(pair)

    print
    print "Total:", len(words)

if __name__ == '__main__':
    main()

