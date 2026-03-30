import os


def script(pth: str):
    if not os.path.exists(pth):
        return "такой папки не существует"
    
    files = os.listdir(pth) # 
    lens = [len(file) for file in files] # [12, 8, 9, 3, 44] 44 = 4
    max_elem = files[lens.index(max(lens))]
    dir_counter = 0
    file_counter = 0

    txt_files = []

    for obj in files:
        if os.path.isdir(obj):
            dir_counter += 1
        else:
            if obj.endswith(".txt"):
                txt_files.append(obj)
            file_counter += 1
        print(f"Название файла: {obj}, размер: {os.path.getsize(obj)}")

    print(dir_counter)
    print(file_counter)
    print(max_elem)

script(os.getcwd())