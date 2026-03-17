# type hint
# аннотации
def greeting(n: int) -> int:
    return n**10

def bgreeting(n: int):
    print(n**10)

number = greeting(int(input()))
print(number // 2)

abc = bgreeting(int(input()))
print(abc)