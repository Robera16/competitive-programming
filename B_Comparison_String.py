for _ in range(int(input())):
    n = int(input())
    g_cnt = 0
    l_cnt = 0
    string = input()
    cost = 0
    stack = []

    for char in string:
        if not stack:
            cost+=2
            stack.append(char)
            if char=='<':
                l_cnt+=1
            else:
                g_cnt+=1
        elif char=='>':
            if stack[-1]=='<' or l_cnt > g_cnt:
                g_cnt +=1
                stack.append(char)
            else:
                cost+=1
                g_cnt +=1
                stack.append(char)
        else:

            if stack[-1]=='>' or g_cnt > l_cnt:
                l_cnt +=1
                stack.append(char)
            else:
                cost+=1
                l_cnt +=1
                stack.append(char)
    print(cost)
