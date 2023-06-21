class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
            from collections import defaultdict
            from queue import Queue
            def topological_sort(graph):
                # Step 1: Calculate in-degree
                in_degree = [0] * len(graph)
                for node in range(len(graph)):
                    for neighbor in graph[node]:
                        in_degree[neighbor] += 1

                # Step 2: Enqueue nodes with in-degree of zero
                queue = Queue()
                for node in range(len(graph)):
                    if in_degree[node] == 0:
                        queue.put(node)

                # Step 3: Perform topological sorting
                result = []
                while not queue.empty():
                    node = queue.get()
                    result.append(node)
                    for neighbor in graph[node]:
                        in_degree[neighbor] -= 1
                        if in_degree[neighbor] == 0:
                            queue.put(neighbor)

                # Step 4: Check for cycles
                if len(result) != len(graph):
                    return []

                return result
            
            graph=[[] for _ in range(numCourses)]
            for u, v in prerequisites:
                graph[v].append(u)
            
            return topological_sort(graph)
                
                
                
                
                
                
