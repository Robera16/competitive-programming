total = 0
for i in range(int(input())):
    inp = list(map(int, input().split()))
    total += inp.count(1)

print(total//2)