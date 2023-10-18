class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0]*(n+1)
        graph = defaultdict(list)
        
        for x, y in relations:
            indegree[y] += 1
            graph[x].append(y)
        
        sol = [0] + time
        time = [0] + time
        q = deque([x for x in range(1, n+1) if not indegree[x]])
        
        while q:
            cur = q.popleft()
            for next_c in graph[cur]:
                sol[next_c] = max(sol[next_c], sol[cur]+time[next_c])
                indegree[next_c] -= 1
                if not indegree[next_c]:
                    q.append(next_c)
        
        return max(sol)
            