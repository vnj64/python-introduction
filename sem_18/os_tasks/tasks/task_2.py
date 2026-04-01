import os


def solve():
    """
    Задание 2: Очистка от временных файлов

    В папке `tasks/data_for_task_2` находится беспорядок из разных файлов.
    Вам нужно написать код, который найдет и удалит все файлы,
    заканчивающиеся на `.tmp`.
    """
    folder = os.path.join("tasks", "data_for_task_2")
    files = os.listdir(folder)

    for file_name in files:
        if file_name.endswith(".tmp"):
            file_path = os.path.join(folder, file_name)
            os.remove(file_path)
