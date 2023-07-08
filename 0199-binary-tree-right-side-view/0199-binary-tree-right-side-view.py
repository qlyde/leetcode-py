# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        visited = set()
        ret = []
        def dfs(root, depth=0):
            nonlocal visited
            nonlocal ret
            if not root:
                return
            if depth not in visited:
                ret.append(root.val)
                visited.add(depth)
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        dfs(root)
        return ret

