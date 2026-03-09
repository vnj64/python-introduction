n = int(input())
counter = 0
for i in range(n):
    st = input()
    if st.count("11") >= 3:
        counter += 1

print(counter)