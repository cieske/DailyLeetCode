class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        n = target[-1]
        sol = []
        last = 0
        for num in target:
            for _ in range(num-last-1):
                sol.extend(['Push', 'Pop'])
            sol.append('Push')
            last = num
        
        return sol
            