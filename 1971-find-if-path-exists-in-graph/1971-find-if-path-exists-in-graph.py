class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(vertex, graph, visited):
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    dfs(neighbour,graph,visited)
        
        
        graph = [[] for _ in range(n)] 
        visited = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        dfs(source, graph,visited)
        
        if destination in visited:
            return True
        return False