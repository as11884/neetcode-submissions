# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        self.inorderTraversalHelper(root, result)
        return result
    
    def inorderTraversalHelper(self, root, result):
        if not root:
            return
        
        self.inorderTraversalHelper(root.left, result)
        result.append(root.val)
        self.inorderTraversalHelper(root.right, result)
        