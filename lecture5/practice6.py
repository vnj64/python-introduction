numbers = [1, 1, 2, 3, 5, 8, 13]  # создаем список

numbers.append(21)  # добавляем число 21 в конец списка
numbers.append(34)  # добавляем число 34 в конец списка

print(numbers) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

numbers = [0, 2, 4, 6, 8, 10]
odds = [1, 3, 5, 7]

numbers.extend(odds) # numbers + odds
print(numbers) # [0, 2, 4, 6, 8, 10, 1, 3, 5, 7]

words1 = ['word1', 'word2', 'word3']
words2 = ['python1', 'python2', 'python3']

words1.append('python')
words2.extend('python')

print(words1) # ['word1', 'word2', 'word3', 'python']
print(words2) # ['python1', 'python2', 'python3', 'p', 'y', 't', 'h', 'o', 'n']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[5]    # удаляем элемент, имеющий индекс 5

print(numbers) # [1, 2, 3, 4, 5, 7, 8, 9]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[2:7] # удаляем элементы с 2 по 6 включительно

print(numbers) # [1, 2, 8, 9]