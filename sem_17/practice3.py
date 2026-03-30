import os

cur = os.getcwd() # текущая папка (str)
files = os.listdir(cur) # список объектов в папке
for file in files: # по сути проходимся по списку строк
    if os.path.isdir(file) == True: # проверяем, что этот объект - строка
        print(f"У файла {file} - размер {os.path.getsize(file)}")