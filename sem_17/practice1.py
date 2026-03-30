import os

print(f"Сейчас мой скрипт работает из папки: {os.getcwd()}") # /home/vnj64/GolandProjects/sandbox_09

os.chdir("sem_17")

print(f"Сейчас мой скрипт работает из папки: {os.getcwd()}") # /home/vnj64/GolandProjects/sandbox_09/sem_17

arr = [16, "kamil", "8952..."]


def namer(s: str = "дефолт", age: int = 20):
    print(f"привет {s}")
    print(f"мне {age} лет")

namer()
namer("камиль")