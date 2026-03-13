numbers = list(range(10, 0, -1))
# 1 способ
for i in range(len(numbers)):
    print(numbers[i])
print()

# 2 способ
for elem in numbers:
    print(elem, end=" ") # 10 9 8 7 6 5 4 3 2 1 
print()

# 3 способ
# можно добавить sep="\n"
# и будет каждое на отдельной строке
print(*numbers) # 10 9 8 7 6 5 4 3 2 1
