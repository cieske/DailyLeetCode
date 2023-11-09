class Solution:
    def countHomogenous(self, s: str) -> int:
        return sum([sum(list(range(len(list(x))+1))) for _, x in groupby(s)]) % (10**9 + 7)
    
    