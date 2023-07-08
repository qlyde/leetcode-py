# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ret = []
        def inOrderTraversal(root, ret):
            if not root:
                return
            inOrderTraversal(root.left, ret)
            ret.append(root.val)
            inOrderTraversal(root.right, ret)
        inOrderTraversal(root, ret)
        return ret[k - 1]
