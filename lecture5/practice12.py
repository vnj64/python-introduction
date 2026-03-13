# невиновные = [0, 3, 6]
# подозреваемые = [0, 1, 3, 4, 8, 10]
# Необходимо из списка подозреваемых удалить невиновных.

innocents = [0, 3, 6]
suspects = [0, 1, 3, 4, 8, 10]

result = []
for susp in suspects:
    if susp not in innocents:
        result.append(susp)

print(result)


i, j = 0, 0
while i < len(innocents):
    if suspects[i] < innocents[j]:
        i+=1