# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0
            lb, ld = dfs(root.left)
            rb, rd = dfs(root.right)
            return lb and rb and abs(ld - rd) <= 1, 1 + max(ld, rd)
        return dfs(root)[0]
