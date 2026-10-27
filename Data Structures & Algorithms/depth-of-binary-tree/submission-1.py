# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # simply put, if root is null, return 0
        if not root:
            return 0
        # then we find the max between going down left or right
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))