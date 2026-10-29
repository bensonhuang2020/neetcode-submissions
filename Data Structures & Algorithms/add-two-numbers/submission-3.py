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
        # non trash way. we use the dummy to keep the head value
        # we keep a carry variable
        # if there's a value to add, we can add them together left to right
        # advance if we do have a value, keep the % as the exact number and the // as the carry. keep creating new nodes.
        def add(l1, l2, carry):
            total = carry
            if not carry and not l1 and not l2:
                return None
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry = total // 10
            total = total % 10

            next_node = add(l1, l2, carry)
            curr_node = ListNode(total)
            curr_node.next = next_node
            return curr_node
        
        return add(l1, l2, 0)
