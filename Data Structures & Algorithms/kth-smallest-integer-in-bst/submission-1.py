# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do dfs and track global variable for counter
        res = 0
        from_k = 0

        def dfs(node):
            nonlocal from_k
            # if there is nothing, we return 0
            if not node:
                return 0
            left_res = dfs(node.left)
            # once we finish the left, if we do have a result, propagate
            if left_res:
                return left_res
            
            # all the while, from the bottom up, we increment the global var and return if we match
            from_k += 1
            if from_k == k:
                return node.val
            right_res = dfs(node.right)
            if right_res:
                return right_res

        return dfs(root)