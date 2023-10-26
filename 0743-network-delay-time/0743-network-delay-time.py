class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
            dist = [float('inf')] * n
            dist[k - 1] = 0

            graph = [[] for _ in range(n)]
            for u, v, w in times:
                graph[u - 1].append((v, w))

            pq = [(0, k)]

            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u - 1]:
                    continue
                for v, w in graph[u - 1]:
                    alt = dist[u - 1] + w
                    if alt < dist[v - 1]:
                        dist[v - 1] = alt
                        heapq.heappush(pq, (alt, v))

            if any(d == float('inf') for d in dist):
                return -1

            return max(dist)