class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [0]*len(graph)
        safe = [0]*len(graph)
        def dfs(node):
            if visited[node]:
                return visited[node] == 2
            
            visited[node] = 1
            for nei in graph[node]:
                if safe[nei]: 
                    pass
                elif visited[nei] or (not visited[nei] and not dfs(nei)):
                    return False
            visited[node] = 2
            
            safe[node] = True
            return True
        
        return [x for x in range(len(graph)) if dfs(x)]
        # sol = []
        # for idx in range(len(graph)):
        #     print(idx)
        #     if dfs(idx): sol.append(idx)
        #     print(visited)
        #     print(safe)
        #     print(sol)
        #     print()