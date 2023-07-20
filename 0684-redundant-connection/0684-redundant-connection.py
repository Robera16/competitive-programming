class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1]*(n+1)
        
        def find(n):
            p = par[n]
            while p!=par[p]:
                par[p]=par[par[p]]
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1==p2:
                return False
            else:
                if rank[p1] > rank[p2]:
                    par[p2]=p1
                    rank[p1]+=rank[p2]
                else:
                    par[p1]=p2
                    rank[p2]+=rank[p1]
                    
                return True
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1,n2]
        