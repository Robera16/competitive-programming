n, t = map(int, input().split())
a = list(map(int, input().split()))

temp = 1+a[0]
flag = False
while temp <= t:
    if temp==t:
        flag = True
        break
    
    temp = temp+a[temp-1]

if flag:
    print('YES')
else:
    print('NO')