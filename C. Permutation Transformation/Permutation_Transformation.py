def find_depths(n, a):
    max_val = max(a)
    idx = a.index(max_val)
    depths = [0] * n
    depths[idx] = 0
    left_a = a[:idx]
    right_a = a[idx + 1:]
    if left_a:
        left_depths = find_depths(len(left_a), left_a)
        for i, d in enumerate(left_depths):
            depths[i] = d + 1
    if right_a:
        right_depths = find_depths(len(right_a), right_a)
        for i, d in enumerate(right_depths):
            depths[idx + 1 + i] = d + 1
    return depths

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    depths = find_depths(n, a)
    print(*depths)