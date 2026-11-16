# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # simple, if there is no root, then we just create treenode for val. otherwise, we check if the node is greater than val, we go left until we can't, etc.
        if not root:
            return TreeNode(val)
        def ins(node):
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    return
                ins(node.left)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return
                ins(node.right)
        
        ins(root)
        return root
                
