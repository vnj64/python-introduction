st = input() # "124135"
counter = 0
ln = len(st) # 6
for i in range(ln):
    # i = index
    counter += int(st[i])
print(counter)

for c in st:
    # c = char
    counter += int(c)
print(counter)

# st[0] "1"
# st[1] "2"
# st[2] "4"
# 3 1
# 4 3 
# 5 5