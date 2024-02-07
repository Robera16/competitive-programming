n = int(input())
string = input()

ones_count = string.count('1')
zeros_count = string.count('0')

print(len(string) - min(ones_count, zeros_count) * 2)
