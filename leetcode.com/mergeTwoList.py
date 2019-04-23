# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2

        if l2 == None:
            return l1

        node = ListNode(0)
        l = node

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        while l1:
            node.next = l1
            l1 = l1.next
            node = node.next

        while l2:
            node.next = l2
            l2 = l2.next
            node = node.next

        return l.next


if __name__ == "__main__":
    a = ListNode(1)
    n = a.next = ListNode(2)
    n.next = ListNode(4)

    b = ListNode(1)
    n = b.next = ListNode(3)
    n.next = ListNode(4)

    s = Solution()
    l = s.mergeTwoLists(a, b)

    print('\nl = ', end=" ")
    while l:
        print(l.val, end=" ")
        l = l.next
