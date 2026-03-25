s = "" # password
count = 0
if len(s) >= 8:
    count += 1
for i in range(len(s)):
    if s[i].isupper():
        count += 1
        continue
    elif s[i].islower():
        count += 1
        continue
    elif s[i].isdigit():
        count += 1
        continue
if count == 4:
    print(True)
else:
    print(False)