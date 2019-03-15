# Delete the Node at a Particular Position in a Linked List

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

    # method for deleting a node having a certain data
    def delete(self, data):
        if not self.head:
            return
        head = self.head
        if head.data == data:
            temp = head.next
            head.next = None
            self.head = temp

        while head:
            if head.next:
                next_node = head.getNext()
                if next_node.getData() == data:
                    head.next = head.next.next
            if head.data == data:
                head.next = None
            head = head.next

    def print_linkedlist(self):
        if not self.head:
            return
        a = self.head
        while a:
            print(a.data)
            a = a.next


if __name__ == '__main__':
    h = Node()
    h.data = 1
    n1 = Node()
    n1.data = 2
    n2 = Node()
    n2.data = 3
    n3 = Node()
    n3.data = 4

    ll = SinglyLinkedList()
    ll.head = h
    a = ll.head
    a.next = n1
    n1.next = n2
    n2.next = n3

    ll.print_linkedlist()
    print("-" * 25)
    ll.delete(4)
    ll.print_linkedlist()
