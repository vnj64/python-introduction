a = int(input()) # 4
result = not a < 10 # True/False
print(result) # False
print(type(result)) # <class 'bool'>


group = "system"
age = 16
if not (age > 16):
    print("можете войти")
else:
    print("доступ запрещен")

num1 = int(input())
st = input()
if 10 < num1:
    print("num1 больше 10")
    if num1 % 2 == 0:
        print("num1 четное число")
    else:
        if st == "kamil":
            print("вас зовут kamil")
        print("num1 нечетное")
else:
    print("num1 меньше 10")