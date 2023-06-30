class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj={i:[] for i in range(numCourses)}

        for x,y in prerequisites:
            adj[y].append(x)
        res=[]
        def dfs(crs):
            if crs not in premap:
                premap[crs]=set()
                for nei in adj[crs]:
                    premap[crs]|=dfs(nei)
            premap[crs].add(crs)
            return premap[crs]

        premap={}
        for i in range(numCourses):
            dfs(i)   
        for x,y in queries:
            res.append(x in premap[y])
        return res