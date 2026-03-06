st = input()
counter = 0
for i in range(len(st) - 1):
    if st[i] == st[i+1]:
        counter += 1
print(counter)