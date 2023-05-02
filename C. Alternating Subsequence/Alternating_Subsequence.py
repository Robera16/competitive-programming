for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    prev_ele, output, flag = arr[0], 0, False
    
    for val in arr:
        if (prev_ele > 0 and val > 0) or (prev_ele < 0 and val < 0):
            if prev_ele < val:
                prev_ele = val
        else:
            output += prev_ele
            prev_ele = val
            flag = True
    
    
    if not flag:
        output = prev_ele
    else:
        output+=prev_ele
        
    print(output)