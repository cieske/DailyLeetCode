# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        lst = [root]
        sol = []
        while lst:
            max_lst = -1*(2**31)-1
            tmp = []
            for node in lst:
                max_lst = max(max_lst, node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            sol.append(max_lst)
            lst = tmp
        
        return sol