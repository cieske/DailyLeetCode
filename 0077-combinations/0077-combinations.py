class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return combinations(list(range(1, n+1)), k)
        