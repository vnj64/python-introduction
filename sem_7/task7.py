st = input()
max_sym = ""
counter = 0
for c in st:
    st_counter = st.count(c)
    if st_counter > counter:
        counter = st_counter
        max_sym = c
print(max_sym)