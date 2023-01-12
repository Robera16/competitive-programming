n = int(input())
string = input()
uniques = list(set(string))
output = []
ck = True
for char in uniques:
    cnt = string.count(char)
    if cnt%n != 0:
        ck = False
        break
    else:
       listt = [char]*(cnt//n)
       output.extend(listt)

if ck:
    print(''.join(output * n))
else:
    print(-1)