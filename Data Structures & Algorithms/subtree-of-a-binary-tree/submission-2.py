# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traverse(rooti: Optional[TreeNode], subRooti: Optional[TreeNode]) -> bool:
            if not rooti and not subRooti:
                return True
            if (not rooti and subRooti) or (rooti and not subRooti):
                return False
            if rooti and subRooti and rooti.val == subRooti.val:
                return (traverse(rooti.left, subRooti.left) and traverse(rooti.right, subRooti.right)) or traverse(rooti.left, subRooti) or traverse(rooti.right, subRooti)
            else:
                return traverse(rooti.left, subRoot) or traverse(rooti.right, subRoot)
        return False or traverse(root, subRoot)