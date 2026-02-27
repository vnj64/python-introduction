num = int(input())

last_digit = num % 10
first_digit = num // 10

if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')