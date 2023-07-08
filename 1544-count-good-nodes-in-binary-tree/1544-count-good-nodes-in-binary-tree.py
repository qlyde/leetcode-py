# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, mx):
            if not root:
                return 0
            ret = 0
            if root.val >= mx:
                ret += 1
                mx = root.val
            ret += dfs(root.left, mx)
            ret += dfs(root.right, mx)
            return ret
        return dfs(root, root.val if root else 0)
