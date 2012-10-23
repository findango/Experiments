#!/usr/bin/env python
# encoding: utf-8
"""
Calculate which words are most common in a 9-letter Wooords game.
"""

import sys

ANAGRAMS = {}
MASK = [0x1, 0x2, 0x4, 0x8, 0x10, 0x20, 0x40, 0x80, 0x100]

def load_dictionary(fname):
    f = open(fname)
    for word in f.readlines():
        word = word.rstrip("\n")
        key = "".join(sorted(word))
        if not ANAGRAMS.has_key(key):
            ANAGRAMS[key] = []
        ANAGRAMS[key].append(word)
    f.close()

def find_anagrams(letters):
    key = "".join(sorted(letters))
    if ANAGRAMS.has_key(key):
        return ANAGRAMS[key][:] # return a copy
    return []

def find_words(letters):
    words = []
    for combo in range(512):
        subset = ""
        for i in range(9):
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
    load_dictionary("./scrabble.txt")

    bingos = filter(lambda w: len(w) == 9, ANAGRAMS.keys())
    word_counts = {}

    for letters in bingos:
        for word in find_words(letters):
            key = "".join(sorted(word))
            if not word_counts.has_key(key):
                word_counts[key] = 0
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


