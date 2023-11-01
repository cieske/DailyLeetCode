# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = []
        stack = [root]
        while stack:
            cur = stack.pop()
            cnt.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        
        cnt = Counter(cnt)
        max_n = max(cnt.values())
        sol = []
        for key, value in zip(cnt.keys(), cnt.values()):
            if value == max_n:
                sol.append(key)
        return sol
    