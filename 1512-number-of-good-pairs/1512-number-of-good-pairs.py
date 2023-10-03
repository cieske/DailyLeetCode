class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        
        return sum([(y*(y-1))//2 for _, y in Counter(nums).items()])