class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for x in range(1, m+1):
            dp[0][x] = dp[0][x-1] + ord(s2[x-1])
        for y in range(1, n+1):
            dp[y][0] = dp[y-1][0] + ord(s1[y-1])
            
        for x in range(1, m+1):
            for y in range(1, n+1):
                if s1[y-1] == s2[x-1]:
                    dp[y][x] = dp[y-1][x-1]
                else:
                    dp[y][x] = min(dp[y-1][x] + ord(s1[y-1]), dp[y][x-1] + ord(s2[x-1]))
        
        return dp[-1][-1]
                    