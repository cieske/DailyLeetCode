class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        import math
        
        sol = -1
        s, e = 1, 10**7
        while s <= e:
            mid = (s+e)//2
            
            runtime = sum([math.ceil(dist[i]/mid) for i in range(len(dist)-1)]) + dist[-1]/mid
            if hour  < runtime:
                s = mid+1
            else:
                sol = mid
                e = mid-1
        return sol
        
            
        
        