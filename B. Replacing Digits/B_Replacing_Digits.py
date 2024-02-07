a = list(input())
s = list(input())
s.sort()

val = s.pop()
for ind, value in enumerate(a):
    if value < val:
        a[ind] = val
        if len(s):
            val = s.pop()
        else:
            break

a = map(str, a)
print(''.join(a))