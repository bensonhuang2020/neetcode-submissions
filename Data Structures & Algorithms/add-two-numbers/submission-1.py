# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # i'm just going to do this the naive way
        """
        num1 = 0
        num2 = 0
        multiple = 1
        while l1:
            num1 += l1.val * multiple
            multiple *= 10
            l1 = l1.next
        
        multiple = 1
        while l2:
            num2 += l2.val * multiple
            multiple *= 10
            l2 = l2.next
        
        res = num1 + num2
        head = ListNode(val = res % 10)
        res = res // 10
        itin = head
        while res:
            itin.next = ListNode(val = res % 10)
            res = res // 10
            itin = itin.next
        return head
        """
        # non trash way
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            tot = val1 + val2 + carry
            carry = tot // 10
            cur.next = ListNode(val=tot % 10)
            cur = cur.next
        return dummy.next