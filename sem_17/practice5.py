import os

linux = "/home/vnj64/GolandProjects/sandbox_09"

print(os.getcwd())

os.chdir("sem_18")
print(os.getcwd())
print(os.listdir())

os.remove("templates/t.py")
os.rmdir("templates")
