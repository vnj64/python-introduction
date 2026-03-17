def is_password_good(password: str) -> bool:
    count = 0
    count_upper = 0
    count_lower = 0
    digit_flag = False
    if len(password) >= 0:
        count += 1
    for i in range(len(password)):
        if password[i].isupper():
            count_upper += 1
        if password[i].islower():
            count_lower += 1
        if password[i].isdigit():
            digit_flag = True
    
    if count_upper > 0:
        count += 1
    if count_lower > 0:
        count += 1
    if digit_flag:
        count += 1
    
    if count == 4:
        return True
    else:
        return False
    
for i in range(5):
    print(is_password_good(input()))