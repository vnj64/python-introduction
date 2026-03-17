def get_days(month: int) -> int:
    if month == 2:
        return 28
    if month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
    

print(get_days(2))