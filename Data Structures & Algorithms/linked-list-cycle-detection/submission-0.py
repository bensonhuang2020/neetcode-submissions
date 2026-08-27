# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            if fast == slow:
                return True
            slow = slow.next
            index += 1
        return False
