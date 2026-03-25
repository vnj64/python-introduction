s = input().split() # ['1', '2', '3']
res = [int(s[i]) for i in range(len(s))] # [1, 2, 3]
# for i in range(len(s)):
#     s[i] = int(s[i])

def is_positive(num: int) -> bool:
    if num >= 0:
        return True
    else:
        return False

def count_positive(numbers: list) -> int:
    count = 0
    for i in range(len(numbers)):
        if is_positive(numbers[i]) == True:
            count += 1

    return count

def count_negative(numbers: list) -> int:
    count = 0
    for i in range(len(numbers)):
        if is_positive(numbers[i]) == False:
            count += 1

    return count

print(count_positive([]))