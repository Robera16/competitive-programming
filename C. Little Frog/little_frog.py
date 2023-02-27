n = int(input())
left, right = 1, n

while left < right:
    print(left,end=" ")
    print(right,end=" ")
    left+=1
    right-=1

if left==right:
    print(left, end="")