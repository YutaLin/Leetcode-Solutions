# Last updated: 7/29/2025, 9:02:28 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traverse(root: TreeNode):
            if not root:
                return
            
            traverse(root.left)
            traverse(root.right)
            ans.append(root.val)
        
        traverse(root)
        return ans