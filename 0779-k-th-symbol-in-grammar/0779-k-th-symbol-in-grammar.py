class Solution:
    def kthGrammar(self, n, k):
        flag = True

        t = 2**(n-1)

        while t != 1:
            t /= 2

            if k > t:
                k -= t
                flag = not flag

        return 0 if flag else 1