# for i in range(int(input())):
#     n, k = map(int, input().split())
#     integers = list(map(int, input().split()))
#     steps = 0
#     while sum(integers) > k:
#         min_index = integers.index(min(integers))
#         max_index = integers.index(max(integers))

#         if integers[min_index]==integers[max_index]:
#             integers[min_index]-=1
#         else:
#             integers[max_index]=integers[min_index]
        
#         steps+=1
    
#         print(integers, steps)

def get_sum_steps(a, k, steps):
    # Calculate the current sum of array a
    current_sum = sum(a)

    # Count the number of steps to set elements to k using the binary search result
    set_steps = 0
    for num in a:
        set_steps += max(0, steps - num)

    # Check if the current sum can be reduced to k using the given number of steps
    return current_sum - set_steps <= k


def minimum_steps(a, k):
    # Binary search to find the minimum number of steps needed
    left, right = 0, max(a) + k
    while left < right:
        mid = (left + right) // 2
        if get_sum_steps(a, k, mid):
            right = mid
        else:
            left = mid + 1
    return left


# Input
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # Output
    print(minimum_steps(a, k))

