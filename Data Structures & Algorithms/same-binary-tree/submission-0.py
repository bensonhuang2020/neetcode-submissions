# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        visited_p = []
        visited_q = []

        def visit_nodes(root: Optional[TreeNode], visited) -> None:
            if not root:
                visited.append(root)
                return
            visited.append(root.val)
            visit_nodes(root.left, visited)
            visit_nodes(root.right, visited)
        
        visit_nodes(p, visited_p)
        visit_nodes(q, visited_q)

        return visited_p == visited_q