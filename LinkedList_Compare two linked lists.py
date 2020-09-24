#!/bin/python3

import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def compare_lists(llist1, llist2):
    res = 0
    cur =llist1
    fur =llist2
    if llist1 == None or llist2 == None:
        res = 0
    while cur.next and fur.next:
        if cur.data==fur.data:
            cur = cur.next
            fur = fur.next
            res = 1
        else:
            res = 0
            break
    return res

if __name__ == '__main__':
