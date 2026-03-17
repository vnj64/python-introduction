def get_last_number(number):
    last_number = number % 10
    return last_number

def get_first_number(number):
    first_number = number // 10
    return first_number

print(get_first_number(34)) # 3
print(get_last_number(12)) # 2

n = get_last_number(52)
print(n**2) # 4