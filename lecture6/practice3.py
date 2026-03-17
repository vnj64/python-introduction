n = int(input())
st = input()

def printer():
    print(st*n)

# при n = 10, st = "abc"
printer() # abcabcabcabcabcabcabcabcabcabc

n = 2
st = "123"

printer() # 123123