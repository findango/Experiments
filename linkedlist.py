#!/usr/bin/env python

import sys 

class Node:
    value = None
    next = None

    def __init__(self, value=None):
        self.value = value

class List:
    head = None
    tail = None

    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def insert(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node

    def find(self, value):
        node = self.head
        while (node is not None):
            if node.value == value:
                return node
            node = node.next
        return None

    def __str__(self):
        string = ""
        node = self.head.next
        while (node is not None):
            string += str(node.value) + ", "
            node = node.next
        return string

def main(argv=None):
    list = List()
    
    list.insert(2)
    list.insert(7)
    list.insert(9)
    list.insert(3)
    list.insert(4)

    print list
    print list.find(17)


if __name__ == "__main__":
    sys.exit(main())

