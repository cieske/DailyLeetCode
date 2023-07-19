class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        min_e = intervals[0][1]
        sol = 0
        
        for start, end in intervals[1:]:
            if min_e <= start:
                min_e = end
            else:
                sol += 1
        
        return sol
            
        