# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        q = deque()
        if root:
            q.append(root)
        while q:
            lvl = []
            for _ in range(len(q)):
                n = q.popleft()
                lvl.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            ret.append(lvl)
        return ret
