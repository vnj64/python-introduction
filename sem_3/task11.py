num1 = int(input())
num2 = int(input())
operation = input("Введите желаемую операцию (+, -, *, /): ")

if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Неизвестная операция")