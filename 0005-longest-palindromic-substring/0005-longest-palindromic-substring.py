class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l_p, r_p):
            while l_p >= 0 and r_p < len(s) and s[l_p] == s[r_p]:
                l_p -= 1
                r_p += 1
            return s[l_p+1:r_p]
        
        sol = ''
        for idx in range(len(s)):
            x = check(idx, idx)
            y = check(idx, idx+1)
            if len(sol) < len(x):
                sol = x
            if len(sol) < len(y):
                sol = y
            
        return sol