from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		
		def dfs(node, visited, parent, adj):
    		visited[node] = True
    
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, visited, node, adj):
                        return True
                elif parent != neighbor:
                    return True
        
            return False


        visited = [False] * V

        for node in range(V):
            if not visited[node]:
                if dfs(node, visited, -1, adj):
                    return 1

        return 0
    

#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends