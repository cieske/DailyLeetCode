class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[i]^pref[i-1] if i > 0 else pref[i] for i in range(len(pref))]