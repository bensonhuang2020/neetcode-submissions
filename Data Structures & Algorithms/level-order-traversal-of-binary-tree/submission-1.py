# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # essentially, this is just bfs but we want to keep tracking the height level
        res = []
        # turn into deque so we can collect and pop
        q = collections.deque()
        q.append(root)

        # bfs
        while q:
            len_q = len(q)
            curr = []
            # takes what was initially in the deque
            for i in range(len_q):
                # remove off the queue front
                curr_node = q.popleft()
                if curr_node:
                    # if there is something, it's all the same level
                    curr.append(curr_node.val)
                    q.append(curr_node.left)
                    q.append(curr_node.right)
            # this is in the case that we have an empty list from empty children
            if curr:
                res.append(curr)
        return res