# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        sol = []
        if not n%2: return sol
        
        self.exist = dict()
        self.exist[1] = [TreeNode(0)]
        
        return self.generate_tree(n)

    
    def generate_tree(self, num_remain):
        if num_remain in self.exist:
            return self.exist[num_remain]

        lst = []
        for i in range(1, num_remain-1, 2):
            l_tree = self.generate_tree(i)
            r_tree = self.generate_tree(num_remain-i-1)

            for left in l_tree:
                for right in r_tree:
                    lst.append(TreeNode(0, left, right))

        self.exist[num_remain] = lst
        return lst
            
                
                