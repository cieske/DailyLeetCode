class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        
        sol = [1]*len(ratings)
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                sol[i] = sol[i-1] + 1
                
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                sol[i-1] = max(sol[i-1], sol[i]+1)
                
        return sum(sol)