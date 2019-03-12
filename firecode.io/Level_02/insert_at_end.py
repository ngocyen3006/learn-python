# Inserting a Node at the End of a Singly Linked List

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

    # method for inserting a new node at the end of a Linked List
    def insertAtEnd(self, data):
        node = Node()
        node.setData(data)

        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNext()


if __name__ == '__main__':
    a = SinglyLinkedList()
    a.insertAtEnd(1)
    a.insertAtEnd(2)
    a.insertAtEnd(4)
    a.insertAtEnd(3)
    a.insertAtEnd(7)
    a.printNode()
