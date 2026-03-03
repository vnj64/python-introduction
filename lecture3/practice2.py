s = 'google.com'
if 'a' in s:
    print('Введенная строка содержит символ а')
else:
    print('Введенная строка не содержит символ а') # выведется это

s = 'google.com'
if 'a' not in s:
    print('Введенная строка не содержит символ а') # выведется это
else:
    print('Введенная строка содержит символ а')

if "5" not in str(max(1, 2, 3, 4, 5)):
    print("5 не содержится в этой строке")
else:
    print("5 содержится в этой строке")

a = "b" in "abcd"
print(a) # True
print("b" not in "abcd") # False