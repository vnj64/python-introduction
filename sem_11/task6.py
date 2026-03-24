def get_factors(num: int) -> list:
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)

    return 10


print(get_factors(int(input())))

