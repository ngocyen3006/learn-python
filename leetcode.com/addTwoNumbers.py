# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    head = ListNode(0)
    l = head
    hold = 0

    while l1 and l2:
        if l1.val + l2.val + hold < 10:
            head.next = ListNode(l1.val + l2.val + hold)
            hold = 0
        else:
            head.next = ListNode((l1.val + l2.val + hold) % 10)
            hold = 1

        l1 = l1.next
        l2 = l2.next
        head = head.next

    while l1:
        if l1.val + hold < 10:
            head.next = ListNode(l1.val + hold)
            hold = 0
        else:
            head.next = ListNode((l1.val + hold) % 10)
            hold = 1

        l1 = l1.next
        head = head.next

    while l2:
        if l2.val + hold < 10:
            head.next = ListNode(l2.val + hold)
            hold = 0
        else:
            head.next = ListNode((l2.val + hold) % 10)
            hold = 1

        l2 = l2.next
        head = head.next

    if hold == 1:
        head.next = ListNode(1)

    return l.next


if __name__ == "__main__":
    a = ListNode(3)
    n = a.next = ListNode(7)
    # nt = n.next = ListNode(4)
    # nt.next = ListNode(2)

    b = ListNode(9)
    n = b.next = ListNode(2)
    # n.next = ListNode(6)

    l = addTwoNumbers(a, b)

    print('\nl = ', end=" ")
    while l:
        print(l.val, end=" ")
        l = l.next
