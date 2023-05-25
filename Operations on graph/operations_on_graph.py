from collections import defaultdict

vertices = int(input())
operations = int(input())

graph = defaultdict(list)

for j in range(operations):
    lst = list(map(int, input().split()))
    
    if lst[0]==1:
        
        graph[lst[1]].append(lst[2])
        graph[lst[2]].append(lst[1])
    
    else:
        if lst[1] in graph:
            print(*graph[lst[1]])