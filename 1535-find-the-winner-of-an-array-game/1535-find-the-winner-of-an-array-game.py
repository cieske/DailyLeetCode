class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        elif k >= len(arr):
            return max(arr)
        
        cnt, sol = 0, arr[0]
        for num in arr[1:]:
            if sol > num:
                cnt += 1
            else:
                cnt = 1
                sol = num
            if cnt == k:
                return sol
        return sol