n = int(input())
for i in range(n):
  a, b = list(map(int, input().split()))
  c = min(a,b)
  d = (a+b) // 4
  print(min(c,d))