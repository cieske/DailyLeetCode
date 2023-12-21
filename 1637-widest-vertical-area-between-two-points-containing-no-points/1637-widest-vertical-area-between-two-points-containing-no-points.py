class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        return max(b-a for a,b in pairwise(sorted([x[0] for x in points])))