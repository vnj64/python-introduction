n = int(input())

base = []
result = []
for i in range(n):
    st = input().lower()
    base.append(st)

query = input().lower()
for i in range(len(base)):
    if query in base[i]:
        result.append(base[i])

print(result)