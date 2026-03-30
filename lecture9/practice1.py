file = open('/home/vnj64/GolandProjects/sandbox_09/lecture9/languages.txt', 'r', encoding='utf-8')

content = file.read()
print(content)
file.close()