# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # so the worst way would be to keep the head, traverse the whole thing and keep the size running, then recount and remove?
        if head.next is None:
            return None
        length = 0
        linked = head
        while linked:
            length += 1
            linked = linked.next
        num_from_back = length - n
        # second pass
        l = 0
        linked2 = head
        # after counting the length, we want to remove the previous pointer's connection
        while l < (length - n - 1):
            l += 1
            linked2 = linked2.next

        # the one edge case is if we're removing the head, there's not going to be a prev for the thead
        if n == length:
            head = head.next
        else:
            linked2.next = linked2.next.next
        return head
