class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c.strip("-").isnumeric():
                stack.append(c)
            else:
                a, b = stack.pop(), stack.pop()
                stack.append(str(int(eval(b + c + a))))
        return int(stack[0])