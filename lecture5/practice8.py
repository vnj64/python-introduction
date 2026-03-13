s = 'Python is the most powerful language'
words = s.split()

# ['Python', 'is', 'the', 'most', 'powerful', 'language']
print(words)

# 1 2 3 4 5
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# [1, 2, 3, 4, 5]
print(numbers)

ip = '192.168.1.24'
numbers = ip.split('.')

print(numbers)

words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
s = ' '.join(words)
# Python is the most powerful language
print(s)

words = ['всем', 'доброе', 'утро']
print('*'.join(words)) # всем*доброе*утро
print('-'.join(words)) # всем-доброе-утро
print('*****'.join(words)) # всем*****доброе*****утро
print('123'.join(words)) # всем123доброе123утро