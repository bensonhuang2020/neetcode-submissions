# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # do dfs
        def validate(node, low, high):
            # if there is nothing, it's a valid bst
            if not node:
                return True
            
            # following the rules, the middle must be larger than the lower, and the higher must be lower than the middle
            if not low < node.val < high:
                return False
            
            # if that's fulfilled, we recursively move down. going left, the values on the left side must be less and the values on the right side must be more than the current node. hence we replace one and not both
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        # start with -inf and +inf since root can be anything.
        return validate(root, float('-inf'), float('inf'))
