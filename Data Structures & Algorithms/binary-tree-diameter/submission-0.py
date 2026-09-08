# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def dep(Node):
            nonlocal diameter
            if Node is None:
                return 0
            left=dep(Node.left)
            right=dep(Node.right)
            diameter = max(diameter,left+right)
            return 1+max(left,right)
        dep(root)
        return diameter

        