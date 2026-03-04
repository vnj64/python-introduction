n = int(input())
n1 = 1
n2 = 0
for i in range(n):
    n2 = n1 + n2
    n1 = n2 - n1
    print(n2,'', end='')

# можно еще так:
n = int(input())
a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b