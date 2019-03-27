# Find the "Nth from the end" Node in a List

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

    def __str__(self):
        return '%s' % self.data


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def find_nth_node_from_end(self, n):
        if not self.head:
            return
        singly_list = []
        current_node = self.head
        while current_node:
            singly_list.append(current_node)
            current_node = current_node.next
        length = len(singly_list)
        if n > length or n < 1:
            return None
        return singly_list[length - n]
