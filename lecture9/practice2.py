file = open('/home/vnj64/GolandProjects/sandbox_09/lecture9/languages.txt', 'r', encoding='utf-8')

print(file.encoding)
print(file.closed)
file.close()
print(file.closed)