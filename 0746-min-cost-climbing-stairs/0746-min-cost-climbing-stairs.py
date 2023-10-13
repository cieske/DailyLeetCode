class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        for i in range(2, len(cost)+1):
            dp.append(min(cost[i-1]+dp[-1], cost[i-2]+dp[-2]))
        return dp[-1]
        