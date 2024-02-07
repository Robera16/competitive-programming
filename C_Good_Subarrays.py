from collections import defaultdict
for _ in range(int(input())):

    n = int(input())
    decimal_digits = input()
    dct = defaultdict(int)
    dct[0] = 1
    prefix_sum = [0]*n
    prefix_sum[0]=decimal_digits[0]
    good_subarrays = 0

    for i in range(1,n):
        prefix_sum[i]=int(prefix_sum[i-1])+int(decimal_digits[i])

    for i in range(n):
        right = int(prefix_sum[i]) - i
        dct[right-1] += 1
        good_subarrays += dct[right-1] - 1
        
    print(good_subarrays)