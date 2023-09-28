class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        o_lst, e_lst = [], []
        
        for num in nums:
            if num % 2:
                o_lst.append(num)
            else:
                e_lst.append(num)
        
        return e_lst + o_lst