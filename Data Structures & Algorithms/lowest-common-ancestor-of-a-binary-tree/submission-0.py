# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # this means that root is the intersection of the two since p and q can be found in left and right (not in order)
        if left and right:
            return root


        # guaranteed that there is an ancestor, so they're in both trees, we work recursively to find the lowest common ancestor.
        return left or right