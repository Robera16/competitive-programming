val = 0
n = int(input())
for i in range(n):
    y=input()
    if y=="X++" or y=="++X":
        val+=1
    if y=="X--" or y=="--X":
        val-=1
print(val)