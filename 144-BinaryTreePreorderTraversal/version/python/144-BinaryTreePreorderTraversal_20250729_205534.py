# Last updated: 7/29/2025, 8:55:34 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traverse(root: TreeNode):
            if not root:
                return
            
            ans.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return ans