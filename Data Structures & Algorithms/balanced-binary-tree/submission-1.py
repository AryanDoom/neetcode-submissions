# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left=height(node.left)
            if left==-1:
                return -1
            right=height(node.right)
            if right == -1:
                return -1
            if abs(right-left)>1:
                return -1
            return 1+max(right,left)
        balls=height(root)
        return balls != -1







        # max_depth=maxDepth(self,root)
        # min_depth=minDepth(root)
        # if max_depth-min_depth>1:
        #     return False
        # return True
        # def minDepth(root) -> int:
        #     if not root:
        #         return 0
        #     if not root.left:
        #         return minDepth(root.right) + 1
        #     if not root.right:
        #         return minDepth(root.left) + 1
        #     return min(minDepth(root.left), minDepth(root.right)) + 1


        # def maxDepth(root: Optional[TreeNode]) -> int:
        #     # depth_height=0
        
        #     # while left in not None:
        #     #     depth_height=depth_height+1
        #     if root is None:
        #         return 0
        #     return 1+(max(maxDepth(root.right),maxDepth(root.left)))

            
        # max_depth=maxDepth(root)
        # min_depth=minDepth(root)
        # if max_depth-min_depth>1:
        #     return False
        # return True
        