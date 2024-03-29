class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack, t_stack = [], []
        for c in s:
            if c != '#':
                s_stack.append(c)
            else:
                if s_stack:
                    s_stack.pop()
        for c in t:
            if c != '#':
                t_stack.append(c)
            else:
                if t_stack:
                    t_stack.pop()
                    
        return s_stack == t_stack
        