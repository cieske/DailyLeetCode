# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.sol = 0
        self.dfs(root, start)
        return self.sol
    
    def dfs(self, root, start):
        if root is None:
            return 0

        l_d = self.dfs(root.left, start)
        r_d = self.dfs(root.right, start)

        if root.val == start:
            self.sol = max(l_d, r_d)
            return -1
        elif l_d < 0 or r_d < 0:
            self.sol = max(self.sol, abs(l_d)+abs(r_d))
            return min(l_d, r_d)-1
        else:
            return max(l_d, r_d)+1