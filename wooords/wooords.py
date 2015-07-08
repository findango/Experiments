#!/usr/bin/env python
# encoding: utf-8
"""
wooords.py - solve a Wooords puzzle

See: http://strayrobotgames.com/wooords/
"""

import sys
from collections import defaultdict

ANAGRAMS = defaultdict(list)

def load_dictionary(fname):
    f = open(fname)
    for word in f.readlines():
        word = word.rstrip("\n")
        key = "".join(sorted(word))
        ANAGRAMS[key].append(word)
    f.close()

def find_anagrams(letters):
    key = "".join(sorted(letters))
    if ANAGRAMS.has_key(key):
        return ANAGRAMS[key][:] # return a copy
    return []

def find_words(special, letters):
    MASK = [0x1, 0x2, 0x4, 0x8, 0x10, 0x20, 0x40, 0x80]
    words = []
    for combo in range(256):
        subset = special
        for i in range(8):
            if combo & MASK[i]:
                subset += letters[i]
        if len(subset) > 3:
            words.extend(find_anagrams(subset))
    return clean(words)

def clean(words):
    words = list(set(words)) # de-dupe
    words.sort()
    return words

def main():
    special = sys.argv[1]
    letters = sys.argv[2]

    load_dictionary("./scrabble.txt")

    words = find_words(special, letters)
    bingos = filter(lambda w: len(w) == 9, words)

    print "\n".join(words)
    print
    print "Found", len(words), "words"
    print "Bingos: " + ", ".join(bingos)


if __name__ == '__main__':
    main()
