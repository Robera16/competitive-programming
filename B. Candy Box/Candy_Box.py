for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dct={}
    for val in a:
        if val in dct:
            dct[val]+=1
        else:
            dct[val]=1
    
    dct = dict(sorted(dct.items(), key = lambda x: x[1], reverse=True))
    selected_counts = set()
    output = 0
    
    for val, freq in dct.items():
        prev = len(selected_counts)
        selected_counts.add(freq)
        if prev!=len(selected_counts):
            output+=freq
            selected_counts.add(freq)
        else:
            freq-=1
            while freq:
                prev = len(selected_counts)
                selected_counts.add(freq)
                if prev!=len(selected_counts):
                    output+=freq
                    break
                else:
                    freq-=1
            
    print(output)