class Solution:
    def halvesAreAlike(self, s: str) -> bool:
     return s[:len(s)//2].count('a')+s[:len(s)//2].count('e')+s[:len(s)//2].count('i')+s[:len(s)//2].count('o')+s[:len(s)//2].count('u')+s[:len(s)//2].count('A')+s[:len(s)//2].count('E')+s[:len(s)//2].count('I')+s[:len(s)//2].count('O')+s[:len(s)//2].count('U') == s[len(s)//2:].count('a')+s[len(s)//2:].count('e')+s[len(s)//2:].count('i')+s[len(s)//2:].count('o')+s[len(s)//2:].count('u')+s[len(s)//2:].count('A')+s[len(s)//2:].count('E')+s[len(s)//2:].count('I')+s[len(s)//2:].count('O')+s[len(s)//2:].count('U')