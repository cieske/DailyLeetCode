class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1], x[0]))
        sol = 1
        end = pairs[0][1]
        
        
        for pair in pairs[1:]:
            if end < pair[0]:
                sol += 1
                end = pair[1]
        
        return sol
            