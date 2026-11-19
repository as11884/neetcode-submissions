# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def levelorder(root, result):
            d = deque([])
            if root:
                d.append(root)
            
            while d:
                levelresult = []
                for i in range(len(d)):
                    root = d.popleft()
                    levelresult.append(root.val)
                    if root.left:
                        d.append(root.left)
                    if root.right:
                        d.append(root.right)
                
                result.append(levelresult)
        
        levelorder(root, result)

        return result
                

    
        