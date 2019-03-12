# Reverse a singly linked list

class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def reverse(self):
        last = None
        current = self.head

        while current:
            next_node = current.next
            current.next = last
            last = current
            current = next_node

        self.head = last
