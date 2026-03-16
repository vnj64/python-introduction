numbers = [8, 9, 10, 11]
del numbers[1]
numbers.insert(1, 17)
numbers.append(4)
numbers.append(5)
numbers.append(6)
del numbers[0]
numbers2 = numbers * 2
numbers2.insert(3, 25)
print(numbers2)
