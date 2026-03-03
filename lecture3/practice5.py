counter = 0
right = int(input())
for i in range(0, right):
    num = int(input())
    if num > 10:
        counter+=1

print(counter)

largest = 0
for _ in range(10):
    num = int(input())    
    if num > largest:
        largest = num

print('Наибольшее число равно', largest)

a = int(input())
b = int(input())
counter = 0
for i in range(a, b+1):
    if (i**3) % 10 == 4 or (i**3) % 10 == 9:
        counter += 1
print(counter)
