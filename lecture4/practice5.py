s = "abcdefgh"
print(s.startswith("a")) # True
print(s.startswith("b")) # False
print(s.startswith("b", 1)) # True

print()

s = "abcdefgh"
print(s.find("d")) # 3
print(s.find("bcde")) # 1

s = "        123 123 123 123        "
# без пробелов в начале и конце
print(s.strip()) # 123 123 123 123

s = "abcde 412 091"
# замена 412 091
print(s.replace("abcde", "замена"))
# abcde a 091
print(s.replace("412", "a"))

