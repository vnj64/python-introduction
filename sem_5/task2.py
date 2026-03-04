# st = input()
# counter = 0
# # пока st != стоп и st != хватит и 
# while ("стоп" not in st) and ("хватит" not in st) and ("достаточно" not in st):
#     st = input()
#     counter += 1

# print(counter)

st = input()
flag = True
counter = 0
while flag:
    counter += 1
    st = input()
    if st == "стоп" or st == "хватит" or st == "достаточно":
        flag = False

print(counter)