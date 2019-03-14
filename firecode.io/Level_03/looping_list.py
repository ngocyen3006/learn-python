# Looping Lists : Space complexity O(1)

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

    def is_cyclic(self):
        head = self.head
        if not head.next:
            return False
        node = head.next
        while node.next:
            if node.data == head.data:
                return True
            node = node.next
        return False
