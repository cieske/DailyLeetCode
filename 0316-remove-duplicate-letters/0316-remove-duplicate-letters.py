class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idx = dict()
        occured = set()
        stack = []
        
        for i in range(len(s)):
            last_idx[s[i]] = i
        
        for idx in range(len(s)):
            if s[idx] not in occured:
                while stack and stack[-1] > s[idx] and last_idx[stack[-1]] > idx:
                    occured.remove(stack.pop())
                
                stack.append(s[idx])
                occured.add(s[idx])
        
        return ''.join(stack)