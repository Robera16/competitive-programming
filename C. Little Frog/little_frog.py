n = int(input())
left = 1
right = n
output = []
while left < right:
    output.append(left)
    output.append(right)
    left+=1
    right-=1

if left==right:
    output.append(left)

print(*output)