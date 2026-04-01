import os


def solve():
    """
    Задание 4: Сбор информации о файлах

    В папке `tasks/data_for_task_4` лежат файлы разных размеров.
    Функция должна вернуть словарь с количеством small, medium и large файлов.
    """
    folder = os.path.join("tasks", "data_for_task_4")
    result = {"small": 0, "medium": 0, "large": 0}
    items = os.listdir(folder)

    for item in items:
        path = os.path.join(folder, item)

        if os.path.isfile(path):
            size = os.path.getsize(path)

            if size <= 100:
                result["small"] += 1
            elif size <= 1000:
                result["medium"] += 1
            else:
                result["large"] += 1

    return result
