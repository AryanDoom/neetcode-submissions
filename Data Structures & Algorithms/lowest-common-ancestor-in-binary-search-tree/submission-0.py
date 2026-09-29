# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root==p or root==q:
            return root
        leftLca=self.lowestCommonAncestor(root.left,p,q) 
        rightLca=self.lowestCommonAncestor(root.right,p,q)
        if leftLca is not None and rightLca is not None:
            return root
        return leftLca if leftLca is not None else rightLca