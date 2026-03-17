def print_fio(name: str, surname: str, patronymic: str):
    result = f"{surname[0] + name[0] + patronymic[0]}".upper()
    result = (surname[0] + name[0] + patronymic[0]).upper()
    print(result)

print_fio("камиль", "камиль", "камиль")
print_fio("ваксима", "Максима", "каксима")
print_fio(input(), input(), input())