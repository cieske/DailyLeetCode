class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for idx, t in enumerate(sorted([(d-1)//s for d, s in zip(dist, speed)])):
            if idx > t:
                return idx
        return idx+1