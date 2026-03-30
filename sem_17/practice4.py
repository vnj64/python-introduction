import os

# /home/vnj64/GolandProjects/sandbox_09
print(os.getcwd())

if not os.path.exists("sem_17") == True:
    print("такой папки не существует")
else:
    os.chdir("sem_17")


files = os.listdir() # ["main.py", ...]
# lens = [len(i) for i in files]
# ind = lens.index(max(lens))
# print(files[ind])

for i in files:
    if os.path.isdir(i) == True:
        os.chdir(i)
        print(i)