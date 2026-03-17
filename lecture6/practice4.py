def ages():
    age = 22
    print(f"Мне {age} лет.")

def max_age():
    print(f"Максиму {age} лет")

def ages():
    print(f"Мне {age} лет.")
    age = 22

ages() # Мне 22 лет.
max_age() # Ошибка: name 'age' is not defined.