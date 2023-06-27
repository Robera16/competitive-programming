
class Solution:
	def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
		
		graph = defaultdict(list)
		in_degree = [0]*n
		res = [set() for _ in range(n)]
		
		# build the graph and count the in degree for each node
		for i in edges:
			graph[i[0]].append(i[1])
			in_degree[i[1]] += 1
		
		que = deque()
		# nodes with an in degree of 0 are added in the que 
		for i in range(len(in_degree)):
			if not in_degree[i]:
				que.append(i)
				
		
		while que:
			node = que.popleft()
			
			for i in graph[node]:
				# since this node is already visited, we can decrease the in degree of it's children by 1 
				in_degree[i] -= 1
				res[i].add(node)
				
				# for the children nodes, we need to add the path of their ancestor 
				for j in res[node]:
					res[i].add(j)
				if not in_degree[i]:
					que.append(i)
					
		for i in range(len(res)):
			res[i] = sorted(res[i])
		   
		return res