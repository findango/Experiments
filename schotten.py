#!/usr/bin/env python
# encoding: utf-8
"""
schotten.py
Show probabilities of completing certain hands in Schotten-Totten.

Created by Finlay Cannon on 2008-06-28.
"""

def bitcount(num):
    total = 0
    while num:
        total +=1
        num = num & (num - 1)
    return total

def probability(need, available):
    wins = 0
    possibilities = 2**available
    for i in range(possibilities):
        if bitcount(i) >= need:
            wins += 1
    return float(wins) / possibilities
    
def main():
    print "        need"
    print "avail      1      2      3"
    print "--------------------------"

    for available in range(1, 7):
        print "   ", available,
        for need in range(1, 4):
            if need <= available:
                print "  %.2f" % probability(need, available),
            else:
                print "     -",
        print 

if __name__ == '__main__':
    main()

