class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0], reverse=True)
        min_s = intervals[0][0]
        sol = 0
        
        for start, end in intervals[1:]:
            if min_s >= end:
                min_s = start
            else:
                sol += 1
        
        return sol
            
        