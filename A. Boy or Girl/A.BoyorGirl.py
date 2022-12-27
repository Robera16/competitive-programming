str=input()
x="".join(set(str))
if len(x)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")