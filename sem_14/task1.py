st = input().split() # "1 2 3 4 5" -> ['1', '2', ...]
for i in range(len(st)):
    st[i] = int(st[i])

def is_positive(num: int) -> bool:
    # должна быть логика определения положительного числа
    return True

def count_positive(numbers: list) -> int:
    count = 0
    for n in numbers:
        if is_positive(n):
            count += 1
    return count

def count_negative(numbers: list) -> int:
    count = 0
    for n in numbers:
        if n < 0:
            # ...
            continue
    return count

print(count_positive(st))
print(count_negative(st))