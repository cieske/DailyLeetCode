class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0], reverse=True)
        lst = [intervals[0]]
        sol = 0
        
        for candi in intervals[1:]:
            if lst[-1][0] >= candi[1]:
                lst.append(candi)
            else:
                sol += 1
        
        return sol
            
        