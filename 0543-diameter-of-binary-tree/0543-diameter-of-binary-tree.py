# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def dfs(root):
            nonlocal ret
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            ret = max(ret, l + r)
            return 1 + max(l, r)
        dfs(root)
        return ret
