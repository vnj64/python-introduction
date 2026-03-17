def convert_grade(grade: int) -> int:
    if grade >= 90:
        return 5
    elif grade >= 80:
        return 4
    elif grade >= 70: 
        return 3
    elif grade >= 60:
        return 2
    else:
        return 1

grade = int(input('Введите вашу отметку: ')) # 67
print(convert_grade(grade)) # 2

def example() -> int:
    return 10
    print(20)
print(example()) # 10
