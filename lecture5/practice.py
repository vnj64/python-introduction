numbers = [2, 4, 6, 8, 10] # список чисел
languages = ['Python', 'C#', 'C++', 'Java'] # список строк
mixed = [2, 'Python', 6, 'Kamil']

for i in range(len(mixed)):
    if isinstance(mixed[i], str):
        print(mixed[i] + "asdasdas")
    if isinstance(mixed[i], int):
        print(mixed[i] ** 2)
    else:
        print("неизвестный тип")