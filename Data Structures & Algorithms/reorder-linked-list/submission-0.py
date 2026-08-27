# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        
        # fast and slow to track what comes halfway
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now we should reverse the latter half which is slow.next to the end
        second = slow.next
        slow.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge the two lists
        merged = head
        second = prev
        while second:
            temp1 = merged.next
            temp2 = second.next
            merged.next = second
            second.next = temp1
            merged = temp1
            second = temp2
        
