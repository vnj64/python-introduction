st = input() # "1 2 3 4 5"
numbers = st.split() # [1 2 3]

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

max1 = max(numbers)
min1 = min(numbers)

max_index = numbers.index(max1)
min_index = numbers.index(min1)

numbers[max_index], numbers[min_index] = min1, max1

for i in range(len(numbers)):
    numbers[i] = str(numbers[i])

print(" ".join(numbers))