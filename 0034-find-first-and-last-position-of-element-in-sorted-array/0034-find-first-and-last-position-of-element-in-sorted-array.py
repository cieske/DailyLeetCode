class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        p1 = bisect.bisect_left(nums, target)
        p2 = bisect.bisect_left(nums, target+1)-1
        
        if p1 == p2+1 and (p1 >= len(nums) or nums[p1] != target):
            return [-1, -1]
        return [p1, p2]