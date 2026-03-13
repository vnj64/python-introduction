# 1 variant
n = int(input())
result = []
for i in range(1, n+1, 2):
    result.append(i)
print(result)

# 2 variant
print(list(range(1, n+1, 2)))

# 3 variant
result1 = []
for i in range(1, n+1):
    if i % 2 != 0:
        result1.append(i)
print(result1)