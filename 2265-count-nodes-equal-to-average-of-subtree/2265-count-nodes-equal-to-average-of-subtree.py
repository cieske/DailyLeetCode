# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def treedp(node):
            child = [node.val]
            sol = 0
            
            if node.left:
                lst, num = treedp(node.left)
                child += lst
                sol += num
            if node.right:
                lst, num = treedp(node.right)
                child += lst
                sol += num
            
            
            if node.val == (sum(child) // len(child)):
                sol += 1
            
            return child, sol
        
        _, sol = treedp(root)
        
        return sol