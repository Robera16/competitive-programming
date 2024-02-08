n, k = map(int, input().split())
ai = list(map(int, input().split()))
l, r, good_segments = 0, 0, 0
frequency = {}

while r < len(ai):
    if ai[r] not in frequency:
        frequency[ai[r]] = 0
    
    frequency[ai[r]]+=1
    
    while len(frequency) > k:
        frequency[ai[l]] -= 1
        if frequency[ai[l]] == 0:
            del frequency[ai[l]]
        l+=1
    good_segments+= r-l+1
    r+=1
    
print(good_segments)