#!/usr/bin/env python
#
# boggle.py - A simple boggle game solver 
#

import sys, getopt, random, copy

BOARD_SIZE = 4
MIN_WORD_LENGTH = 3
DICTIONARY = {}
PREFIXES = {}
DICE = ["aaeegn",
        "abbjoo",
        "achops",
        "affkps",
        "aoottw",
        "cimotu",
        "deilrx",
        "delrvy",
        "distty",
        "eeghnw",
        "eeinsu",
        "ehrtvw",
        "eiosst",
        "elrtty",
        "himnqu",
        "hlnnrz"]


def load_dictionary(filename="dictionary.txt"):
    try:
        f = open(filename)
        for word in f.readlines():
            word = word.rstrip("\n")
            DICTIONARY[word] = True
            while len(word):
                word = word[:-1]
                PREFIXES[word] = True 
        f.close()
    except Exception, e:
        print "Error loading dictionary '%s': %s" % (filename, e)
        sys.exit(1)

def pick_letter(dice):
    die = dice.pop(random.choice(range(len(dice))))
    letter = die[random.choice(range(len(die)))]
    return letter

def init_board(str_board=None):
    board = []
    remaining_dice = DICE[:]
    
    for row in range(BOARD_SIZE):
        board.append([])
        for col in range(BOARD_SIZE):
            if str_board is None:
                letter = pick_letter(remaining_dice)
            else:
                letter = str_board[(row * BOARD_SIZE) + col]
            if letter == "q": letter = "qu"
            board[row].append(letter)
    return board
    
def print_board(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            print "%2s" % board[row][col],
        print

def score_word(word):
    if len(word) == 3: return 1
    if len(word) <  7: return len(word) - 3
    if len(word) == 7: return 5
    if len(word) >  7: return 11

def out_of_bounds(row, col):
    if row < 0 or row > BOARD_SIZE - 1 \
    or col < 0 or col > BOARD_SIZE - 1:
        return True
    else:
        return False

def mark_as_visited(row, col, board):
    board[row][col] = None
    
def already_visited(row, col, board):
    return board[row][col] == None

def is_valid_prefix(prefix):
    return PREFIXES.has_key(prefix)
    
def is_valid_word(word):
    return DICTIONARY.has_key(word) and len(word) >= MIN_WORD_LENGTH

# Mmmm... recursion.        
def seek_from(row, col, board, words, letters=""):
    if out_of_bounds(row, col) or already_visited(row, col, board):
        return

    letters = letters + board[row][col]
    mark_as_visited(row, col, board)
    
    if is_valid_word(letters):
        words[letters] = True

    if is_valid_prefix(letters):
        for delta_row in [-1,0,1]:
            for delta_col in [-1,0,1]:
                seek_from(row + delta_row, col + delta_col, copy.deepcopy(board), words, letters)
        
def solve(board):
    found_words = {}
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            seek_from(row, col, copy.deepcopy(board), found_words)
    words = found_words.keys()
    words.sort()
    return words

    
def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) > 1: 
        letters = argv[1]
    else: 
        letters = None
    
    load_dictionary()
    board = init_board(letters)
    words = solve(board)

    print_board(board)
    print
    print "Found %i words" % len(words)
    for word in words:
        print "%2i  %s" % (score_word(word), word)

    
if __name__ == "__main__":
    sys.exit(main())
