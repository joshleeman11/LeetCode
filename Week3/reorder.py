# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        l1, l2 = head, prev
        while l2.next:
            l1.next, l1 = l2, l1.next
            l2.next, l2 = l1, l2.next


def create_linked_list(values):
    head = ListNode(values[0])
    curr = head
    for value in values[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    return head

def print_linked_list(head: Optional[ListNode]):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Create a linked list from the input list
head = create_linked_list([1, 2, 3, 4])
sol = Solution()
sol.reorderList(head)
print_linked_list(head) 
