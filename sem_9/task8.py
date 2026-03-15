n = int(input())
result = []
for i in range(n):
    st = input()
    if st not in result:
        result.append(st)

print(*result, end="\n")