class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return t != 1 if (fx == sx and fy == sy) else max(abs(fx-sx), abs(fy-sy)) <= t