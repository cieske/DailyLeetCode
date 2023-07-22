class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dx = [1, 2, 2, 1, -1, -2, -2, -1]
        dy = [2, 1, -1, -2, -2, -1, 1, 2]
        field = [[0]*n for _ in range(n)]
        reach = [[0]*n for _ in range(n)]
        reach[row][column] = 1
        
        for _ in range(k):
            for y in range(n):
                for x in range(n):
                    for i in range(8):
                        n_y = y + dy[i]
                        n_x = x + dx[i]
                        if (0 <= n_y < n) and (0 <= n_x < n):
                            field[n_y][n_x] += reach[y][x] / 8
            reach = field
            field = [[0]*n for _ in range(n)]
        
        sol = 0
        for y in range(n):
            for x in range(n):
                sol += reach[y][x]
        return sol
        
        