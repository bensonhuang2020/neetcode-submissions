# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if they're both None, we're done
        if not p and not q:
            return True
        # if they both exist and they're the same, we can recursively check both sides
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # the else is in the case that p and not q or not p and q or p.val != q.val
        else:
            return False