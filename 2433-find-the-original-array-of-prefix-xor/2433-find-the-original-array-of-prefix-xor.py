class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        sol = [pref[0]]
        for i in range(1, len(pref)):
            sol.append(pref[i-1]^pref[i])
        return sol