# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next
        return l == l[::-1]


def create_linked_list(values):
    head = ListNode(values[0])
    curr = head
    for value in values[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    return head

# Create a linked list from the input list
head = create_linked_list([1, 2, 2, 1])
sol = Solution()
print(sol.isPalindrome(head))
