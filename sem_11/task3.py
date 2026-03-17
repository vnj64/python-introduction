def print_case_counts(s: str):
    count_lower = 0
    count_upper = 0
    for c in s:
        count_upper += c.isupper()
        count_lower += c.islower()

    # for i in range(len(s)):
    #     if s[i].isupper():
    #         count_upper += 1
    print(f"Букв в нижнем регистре: {count_lower}")
    print(f"Букв в верхнем регистре: {count_upper}")

print_case_counts(input())