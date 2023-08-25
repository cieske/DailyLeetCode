class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        self.dp = [[-1]*(len(s2)+1) for _ in range(len(s1)+1)]
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        
        return self.solve(0, 0)

    
    def solve(self, idx1, idx2):
        if idx1 + idx2 == len(self.s3):
            return True
        
        if self.dp[idx1][idx2] != -1: # visited
            return self.dp[idx1][idx2] == 1
        
        
        flag = False
        # s1 assign
        if idx1 < len(self.s1) and self.s1[idx1] == self.s3[idx1+idx2]:
            flag |= self.solve(idx1+1, idx2)
        
        # s2 assign
        if idx2 < len(self.s2) and self.s2[idx2] == self.s3[idx1+idx2]:
            flag |= self.solve(idx1, idx2+1)
        
        
        if flag: # 가능!
            self.dp[idx1][idx2] = 1
        else:
            self.dp[idx1][idx2] = 0
            
        return flag