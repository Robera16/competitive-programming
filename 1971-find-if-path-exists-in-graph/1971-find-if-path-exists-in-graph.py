class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
            graph = collections.defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            visited = set([source])
            queue = deque([source])

            while(len(queue)):
                node = queue.popleft()
                if node==destination:
                    return True

                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)

            return False