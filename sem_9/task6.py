n = int(input())
result = []
for i in range(n):
    num = int(input())
    result.append(num)
print(result)

del result[1::2]
# del result[0]
print(result)