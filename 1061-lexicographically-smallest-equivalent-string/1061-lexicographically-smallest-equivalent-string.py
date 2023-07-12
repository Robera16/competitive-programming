class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(e):
            if e not in parent:
                parent[e] = e
            while e!= parent[e]:
                e = parent[e]
            return e #Returning the root value of e
        
        def union(a,b):
            ra,rb=find(a),find(b)# Sending a &b values to fetch root values
            if ra == rb:
                return
            parent[ra] = parent[rb] = min(ra, rb)#assign the MIN value to both roots in dict (parent)
        
        parent={} # Created a dict to store the root values
        print(zip(s1,s2))
        for c1,c2 in zip(s1,s2): 
            union(c1,c2) #Sending zipped values to UNION function
        return ''.join(parent[find(c)] for c in baseStr)