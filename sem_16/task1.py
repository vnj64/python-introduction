s = input().split()
numb = [int(s[i]) for i in range(len(s))]

def is_zero(num: int) -> bool:
    if num == 0:
        return True
    else:
        return False

def count_zeros(numbers: list) -> int:
    count = 0
    for i in range(len(numbers)):
        if is_zero(numbers[i]):
            count += 1

    return count

def count_non_zeros(numbers: list) -> int:
    count = 0
    for i in range(len(numbers)):
        if not is_zero(numbers[i]):
            count += 1

    return count

print(count_zeros(numb))
print(count_non_zeros(numb))