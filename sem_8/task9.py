n = int(input())

# во имя отрицательных тестов мы тут пишем int(input())
first = 0
second = 0

for i in range(n):
    x = int(input())

    if x > first:
        second = first
        first = x
    # 0 < 9 < 10
    elif second < x < first:
        second = x
        first = second
# n = 4
# 9
# 9
# 10
# 10
print(first)
print(second)