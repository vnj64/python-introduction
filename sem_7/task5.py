# 1 variant
st = input()
counter = 0
# for c in st:
#     if c in "0123456789":
#         counter += 1
# print(counter)


# 2 variant
for i in range(len(st)):
    if st[i].isdigit():
        counter += 1

# Kamil
for c in st:
    if c.isdigit():
        counter += 1

print(counter)
