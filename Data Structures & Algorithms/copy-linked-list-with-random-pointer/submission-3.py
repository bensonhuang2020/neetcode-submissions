"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # easiest way is to set up another list to hold each of the new nodes when you make them, then they should point to the nodes in the list
        if not head:
            return None

        # hashmap solution
        """
        node_dict = {}
        first = head
        while first:
            node_dict[first] = Node(x = first.val)
            first = first.next
        second = head
        while second:
            if second.next is None:
                node_dict[second].next = None
            else:
                node_dict[second].next = node_dict[second.next]
            if second.random is None:
                node_dict[second].random = None
            else:
                node_dict[second].random = node_dict[second.random]
            second = second.next
        
        return node_dict[head]
        """
        # alternative solution in place
        cur = head
        # directly put the replacement right after the original
        while cur:
            new = Node(cur.val)
            new.next = cur.next
            cur.next = new
            cur = new.next
        
        new = head.next

        # if there is a copy, it should appear right after
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        while cur:
            copy = cur.next
            cur.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            cur = cur.next

        return new

        