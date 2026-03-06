s = "abcdefg"
s = "1" + s[1:]
print(s) # 1bcdefg

s = s[:3] + "4" + s[5:]
print(s) # 1bc4fg