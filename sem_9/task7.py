n = int(input())
lst1 = [] # +
lst2 = [] # -
lst3 = [] # 0
for i in range(n):
    num = int(input())
    if num > 0:
        lst1.append(num)
    elif num < 0:
        lst2.append(num)
    else:
        lst3.append(num)
print(lst2)
print(lst3)
print(lst1)