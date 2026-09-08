# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth_height=0
    
        # while left in not None:
        #     depth_height=depth_height+1
        if root is None:
            return 0
        return 1+(max(self.maxDepth(root.right),self.maxDepth(root.left)))

        