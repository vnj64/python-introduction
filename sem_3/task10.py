a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Равносторонний треугольник")
if a != b and a != c and b != c:
    print("Разносторонний треугольник")
else:
    print("Равнобедренный")