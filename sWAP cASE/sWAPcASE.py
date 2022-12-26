def swap_case(s):
    new_str=""
    for val in s:
        if val.isupper():
            new_str+=val.lower()
        else:
            new_str+=val.upper()
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)