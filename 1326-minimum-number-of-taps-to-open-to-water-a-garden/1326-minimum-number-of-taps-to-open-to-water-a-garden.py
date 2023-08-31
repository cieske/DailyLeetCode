class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        lst = sorted([[i-r, i+r] for i, r in enumerate(ranges)], key=lambda x: x[0])
        
        max_cover, idx, sol = 0, 0, 0
        while idx < len(ranges) and max_cover < n:
            if max_cover < lst[idx][0]:
                return -1
            
            cur_max = lst[idx][1]
            while idx < len(ranges) and lst[idx][0] <= max_cover:
                cur_max = max(cur_max, lst[idx][1])
                idx += 1
            
            max_cover = cur_max
            sol += 1
        
        if max_cover < n:
            return -1
        return sol