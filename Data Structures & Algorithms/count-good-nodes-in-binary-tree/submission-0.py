# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # find max so far for each traversal, everything below should be higher valued
        # hence, every call should check if we're greater than the max seen coming down from up. otherwise, we fail anyways.
        def dfs(node, maxSoFar):
            # if null, there is nothing anyways
            if not node:
                return 0
            
            # if we are greater, we are valid
            if node.val >= maxSoFar:
                res = 1
            else:
                res = 0
            # we still want to collect the value
            maxSoFar = max(maxSoFar, node.val)
            # doing left and then right means we completely traverse with dfs
            res += dfs(node.left, maxSoFar)
            res += dfs(node.right, maxSoFar)
            return res
        return dfs(root, root.val)