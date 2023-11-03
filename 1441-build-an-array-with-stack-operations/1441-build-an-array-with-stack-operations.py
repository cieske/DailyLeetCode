class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        return ''.join([' Push Pop'*(([0]+target)[i] - ([0]+target)[i-1] - 1) + ' Push' for i in range(1, len(target)+1)]).strip().split(" ")