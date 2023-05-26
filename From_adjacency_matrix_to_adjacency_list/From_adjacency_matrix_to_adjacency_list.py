from collections import defaultdict

def convert(a):
    
    for i in range(len(a)):
        adjList = []
        adjList.append(a[i].count('1'))
        for ind, val in enumerate(a[i]):
            if val=='1':
                adjList.append(ind+1)
                
        print(*adjList)


n = int(input())
a = []
for  j in range(n):
    a.append(list(input().split()))

convert(a)