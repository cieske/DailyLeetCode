class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict, deque
        
        def dfs(city):
            while flight[city]:
                dfs(flight[city].pop())
            sol.appendleft(city)
            
            
        flight = defaultdict(list)
        for s, e in tickets:
            flight[s].append(e)
        
        for s in flight:
            flight[s].sort(reverse=True)
        
        
        sol = deque([])        
        dfs("JFK")     
        
        return sol