num1 = 17.89
num2 = -13.55
num3 = int(num1)
num4 = int(num2)
print(num3) # 17
print(num4, "\n") # 13

num5 = 17 # int
print(float(num5), "\n") # 17.0

a = max(3, 8, -3, 12, 9)
b = min(3, 8, -3, 12, 9)
c = max(3.14, 2.17, 9.8)
print(a) # 12
print(b) # -3
print(c, "\n") # 9.8

print(abs(10)) # 10
print(abs(-7)) # 7
print(abs(0)) # 0
print(abs(-17.67), "\n") # 17.67

name = "Камиль"
print(f"Длина строки name: {len(name)}") # 6

full_name = "   " # тут 3 пробела
print(f"Длина строки full_name: {len(full_name)}") # 3