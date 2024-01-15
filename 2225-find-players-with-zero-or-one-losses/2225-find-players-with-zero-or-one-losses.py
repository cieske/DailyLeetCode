class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = set()
        lost = defaultdict(int)
        
        for x, y in matches:
            win.add(x)
            lost[y] += 1
        
        for w in list(win):
            if lost[w]:
                win.remove(w)
        
        lose = []
        for l in lost:
            if lost[l] == 1:
                lose.append(l)
        
        return [sorted(list(win)), sorted(lose)]