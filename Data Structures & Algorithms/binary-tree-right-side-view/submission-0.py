# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # run bfs and keep the right most or the last added into the deque
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            q_len = len(q)
            for i in range(q_len):
                last_node = q.popleft()
                if last_node:
                    if last_node.left:
                        q.append(last_node.left)
                    if last_node.right:
                        q.append(last_node.right)
            if last_node:
                res.append(last_node.val)
        return res