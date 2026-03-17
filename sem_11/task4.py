def summa(lst: list) -> float:
    return sum(lst)

def average(lst: list) -> float:
    return summa(lst) / len(lst)

array = [0, 4, 20, 1, 42]
print(average(array))