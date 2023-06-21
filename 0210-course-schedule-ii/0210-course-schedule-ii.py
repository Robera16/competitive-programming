class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
           
            from queue import Queue
            def topological_sort(graph):
                
                in_degree = [0] * len(graph)
                for node in range(len(graph)):
                    for neighbor in graph[node]:
                        in_degree[neighbor] += 1

                queue = deque()
                for node in range(len(graph)):
                    if in_degree[node] == 0:
                        queue.append(node)

                result = []
                while len(queue):
                    node = queue.popleft()
                    result.append(node)
                    for neighbor in graph[node]:
                        in_degree[neighbor] -= 1
                        if in_degree[neighbor] == 0:
                            queue.append(neighbor)

               
                if len(result) != len(graph):
                    return []

                return result
            
            graph=[[] for _ in range(numCourses)]
            for u, v in prerequisites:
                graph[v].append(u)
            
            return topological_sort(graph)
                
                
                
                
                
                
