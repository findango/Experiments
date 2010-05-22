#!/usr/bin/env python
#
# hexdump.py - A quick and dirty formatted hex dump of a file to the console
#

import sys
        
def format_hex(bytes):
    hex_values = map(lambda b:"%02x" % ord(b), bytes) 
    return " ".join(hex_values)


def format_str(bytes):
    chars = map(lambda b:strip_control_chars(b), bytes) 
    return "".join(chars)


def strip_control_chars(char):
    if ord(char) < 32:
        return "."
    return char

    
def main(argv=None):
    if argv is None:
        argv = sys.argv

    file = open(argv[1], "rb")

    LINE_SIZE = 16
    count = 0
    while True:
        bytes = file.read(LINE_SIZE)
        if not bytes:
            break
        print "%08i  %-47s  %s" % (count, format_hex(bytes), format_str(bytes))
        count += LINE_SIZE


if __name__ == "__main__":
    main();

