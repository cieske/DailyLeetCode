class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        sol = n
        
        
        for i in range(len(nums)):
            l_p = nums[i]
            j = bisect_right(nums, l_p+n-1)
            sol = min(sol, n+i-j)
        
        return sol