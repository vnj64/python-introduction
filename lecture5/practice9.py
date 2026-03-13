names = ['Gvido', 'Roman', 'Timur']
print(names) # ['Gvido', 'Roman', 'Timur']
names.insert(0, 'Anders')
print(names) # ['Anders', 'Gvido', 'Roman', 'Timur']
names.insert(3, 'Josef')
print(names) # ['Anders', 'Gvido', 'Roman', 'Josef', 'Timur']

names = ['Gvido', 'Roman', 'Timur']
position = names.index('Timur')
print(position) # 2

food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
print(food) # ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
food.remove('Рис')
print(food) # ['Курица', 'Рыба', 'Брокколи', 'Рис']

names = ['Gvido', 'Roman', 'Timur']
item = names.pop(1)
print(item)
print(names)

names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
cnt1 = names.count('Timur')
cnt2 = names.count('Gvido')
cnt3 = names.count('Josef')

print(cnt1) # 3
print(cnt2) # 1
print(cnt3) # 0