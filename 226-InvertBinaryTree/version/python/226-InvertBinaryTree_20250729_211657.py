# Last updated: 7/29/2025, 9:16:57 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        def invert(root):
            if not root:
                return
            left = root.left
            root.left = root.right
            root.right = left
            
            invert(root.left)
            invert(root.right)

        invert(root)
        return root