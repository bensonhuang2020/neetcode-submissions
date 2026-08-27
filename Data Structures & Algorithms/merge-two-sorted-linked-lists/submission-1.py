# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        curr = head
        list1_curr = list1
        list2_curr = list2
        while list1_curr and list2_curr:
            if list1_curr.val <= list2_curr.val:
                curr.next = list1_curr
                list1_curr = list1_curr.next
            else:
                curr.next = list2_curr
                list2_curr = list2_curr.next
            curr = curr.next
        if not list1_curr:
            curr.next = list2_curr
        else:
            curr.next = list1_curr
        return head
