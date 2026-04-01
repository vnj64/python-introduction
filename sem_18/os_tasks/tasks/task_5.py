import os


def solve():
    """
    Задание 5: Поиск текстовых файлов в папке

    В папке `tasks/data_for_task_5` нужно найти только файлы `.txt`,
    которые лежат прямо в этой папке.
    """
    folder = os.path.join("tasks", "data_for_task_5")
    result = []
    items = os.listdir(folder)

    for item in items:
        path = os.path.join(folder, item)

        if os.path.isfile(path) and item.endswith(".txt"):
            result.append(item)

    result.sort()
    return result
