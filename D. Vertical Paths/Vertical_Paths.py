for _ in range(int(input())):
    n = int(input())
    parents=list(map(int, input().split()))
    if n==1:
        # no of paths
        print(1)
        # len of each path(count of vertices)
        print(1)
        # content of each path
        print(1)
        print()
        continue
    
    leaf_node=[True]*(n+1)
    leaf_node[0] = False
    for i in parents:#anything in parents array is not leaf
        leaf_node[i]=False
        
    #num of paths equals num of leaf nodes
    print(leaf_node.count(True))
    
    for vertex, is_leaf_node in enumerate(leaf_node):
        path=[]
        if is_leaf_node==True:
            while parents[vertex-1] != -1 and parents[vertex-1]!=vertex:
                path.append(vertex)
                temp=vertex
                vertex=parents[vertex-1]
                parents[temp-1]=-1
            if parents[vertex-1] != -1:
                path.append(vertex)
                parents[vertex-1]=-1
            # num of vertices in the path
            print(len(path))
            # actual path
            path.reverse()
            print(*path)
    print()