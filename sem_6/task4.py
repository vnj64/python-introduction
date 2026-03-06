st = input()

plus_counter = 0
multiple_counter = 0

for c in st:
    if c == "+":
        plus_counter += 1
    elif c == "*":
        multiple_counter += 1

print(f"{plus_counter}")
print(f"{multiple_counter}")

print(st.count("+"))
print(st.count("*"))