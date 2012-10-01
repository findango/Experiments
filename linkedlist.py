#!/usr/bin/env python

import sys 

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return "[Node value=" + str(self.value) + "]"


class SortedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        prev = None
        current = self.head
        while current is not None and current.value <= value:
            prev = current
            current = current.next

        new_node = Node(value, current)
        if prev is None:
            self.head = new_node
        else:
            prev.next = new_node
    
    def find(self, value):
        node = self.head
        while (node is not None):
            if node.value == value:
                return node
            node = node.next
        return None

    def __str__(self):
        string = ""
        node = self.head
        while (node is not None):
            string += str(node.value)
            if node.next is not None:
                string += ", "
            node = node.next
        return string


def main(argv=None):
    list = SortedList()
    
    list.insert(5)
    list.insert(2)
    list.insert(7)
    list.insert(9)
    list.insert(4)
    list.insert(3)

    print list
    print "find 6:", list.find(6)
    print "find 7:", list.find(7)

if __name__ == "__main__":
    sys.exit(main())

