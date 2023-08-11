class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount: return 1
        
        dp = [0]*(amount+1)
        dp[0] = 1
        
#         for money in range(1, amount+1):
#             for coin in coins:
#                 if coin <= money:
#                     dp[money] += dp[money-coin]
        
#         return dp[-1]
        
        for coin in coins:
            for money in range(coin, amount+1):
                dp[money] += dp[money-coin]
        
        return dp[-1]
            
    