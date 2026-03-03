start = int(input())
stop = int(input()) # 10+1

# 0, 1...(stop - 1) 
for num in range(stop):
    print(num)

print()

for i in range(start, stop-1):
    print(i)

print()

for i in range(start, stop-1, -1):
    print(i)

print()

for i in range(1, 20, 2):
    print(i)

for i in range(10):
    i ** 2
    sum = sum + (i**2)

print()