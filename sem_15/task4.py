def hackers_func(hackers: list, security_level: int, increase: int) -> list:
    if len(hackers) == 0:
        return 0
    success = 0
    for level in hackers:
        if level <= security_level:
            security_level += increase
        else:
            success += 1
    
    return success

print(hackers_func([10, 8, 3, 11, 24], 8, 1))
print(0)