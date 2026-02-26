abc = int(input()) # 345
c = abc % 10 # 5
b = (abc // 10) % 10 # 4
b = (abc % 100) // 10
a = abc // 100 # 3
print(str(a)+str(c)+str(b))