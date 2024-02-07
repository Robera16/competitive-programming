n, s = map(int, input().split())
ai = list(map(int, input().split()))
summ, counter, l = 0, 0, 0

for r in range(len(ai)):
    summ+=ai[r]
    while summ >= s:
        counter+= n-r
        summ-=ai[l]
        l+=1
    
print(counter)
    




# for r in range(len(ai)):
#     summ+=ai[r]
#     temp=summ
#     if summ >= s:
#         count+=1
#     while summ-ai[l] >= s:
#         count+=1
#         summ-=ai[l]
#         l+=1
#     l=0
#     summ=temp
    
# print(count)
    