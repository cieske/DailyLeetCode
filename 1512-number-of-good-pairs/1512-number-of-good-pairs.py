class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum([(y*(y-1))//2 for _, y in Counter(nums).items()])