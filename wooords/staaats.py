#!/usr/bin/env python
# encoding: utf-8
"""
Calculate which words are most common in a 9-letter Wooords game.
"""

import sys
from collections import defaultdict

ANAGRAMS = defaultdict(list)
BIT = [0x1, 0x2, 0x4, 0x8, 0x10, 0x20, 0x40, 0x80, 0x100]
bits = range(9)
combos = range(512)

def load_dictionary(fname):
    f = open(fname)
    for word in f.readlines():
        word = word.rstrip("\n")
        key = "".join(sorted(word))
        ANAGRAMS[key].append(word)
    f.close()

def find_words(letters):
    words = []
    for combo in combos:
        subset = ""
        for i in bits:
            if combo & BIT[i]:
                subset += letters[i]

        if len(subset) > 3 and subset in ANAGRAMS:
            # don't need to sort because we preserved the order of letters 
            #words.extend(ANAGRAMS[subset])
            words.append(subset)
    return clean(words)

def clean(words):
    words = list(set(words)) # de-dupe
    return words


def main():
    load_dictionary("./scrabble.txt")

    bingos = filter(lambda w: len(w) == 9, ANAGRAMS.keys())
    word_counts = defaultdict(int)

    for letters in bingos:
        for word in find_words(letters):
            key = "".join(sorted(word))
            word_counts[key] += 1

    top = sorted(word_counts, key=word_counts.get, reverse=True)[:100]
    
    rk = 1
    for w in top:
        print str(rk) + ".",
        print ", ".join(sorted(ANAGRAMS["".join(sorted(w))])),
        print "(" + str(word_counts[w]) + ")"
        rk += 1

if __name__ == '__main__':
    main()


