class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        
        sol = []
        
        del_pq = []
        cur_pq = []
        for i in range(k):
            heapq.heappush(cur_pq, -nums[i])
        sol.append(-cur_pq[0])
        
        
        for i in range(k, len(nums)):
            heapq.heappush(del_pq, -nums[i-k])
            heapq.heappush(cur_pq, -nums[i])
            
            while len(cur_pq) > k and cur_pq[0] == del_pq[0]:
                heapq.heappop(del_pq)
                heapq.heappop(cur_pq)
            sol.append(-cur_pq[0])
        
        return sol
        
        