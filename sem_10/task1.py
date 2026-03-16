# 192.168.0.1
st = input().split(".")
count = 0

for i in range(len(st)):
    if 0 <= int(st[i]) <= 255:
        count += 1

if count == 4:
    print("ДА")
else:
    print("НЕТ")
