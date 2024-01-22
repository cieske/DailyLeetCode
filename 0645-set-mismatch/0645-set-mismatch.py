class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sorted(Counter(nums).items(), key=lambda x:x[1])[-1][0], (set([x for x in range(1, len(nums)+1)])-set(nums)).pop()]