# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# RECURSIVE DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# # ITERATIVE DFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         stack = [[root, 1]]
#         ret = 0

#         while stack:
#             n, d = stack.pop()

#             if node:
#                 ret = max(ret, d)
#                 stack.append([node.left, d + 1])
#                 stack.append([node.right, d + 1])
#         return res

# # BFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         q = deque()
#         if root:
#             q.append(root)

#         level = 0
#         while q:
#             for i in range(len(q)):
#                 n = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             level += 1
#         return level
