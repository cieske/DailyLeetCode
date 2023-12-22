class Solution:
    def maxScore(self, s: str) -> int:
        return max(s[:idx].count('0') + s[idx:].count('1') for idx in range(1, len(s)))