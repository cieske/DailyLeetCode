class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        sol = [0]*n
        stack = []
        
        for idx in range(len(temperatures)-1, -1, -1):
            cur = temperatures[idx]
            
            while stack and cur >= temperatures[stack[-1]]:
                stack.pop()
                
            if stack:
                sol[idx] = stack[-1]-idx
            stack.append(idx)
        
        return sol