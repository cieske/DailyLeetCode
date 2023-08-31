class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        sol = 0
        min_cover, max_cover = 0, 0
        
        while max_cover < n:
            for idx, r in enumerate(ranges):
                if idx-r <= min_cover and idx+r >= max_cover:
                    max_cover = idx+r
                    
            if min_cover == max_cover:
                return -1
            
            sol += 1
            min_cover = max_cover
        
        return sol