import os


def solve():
    """
    Задание 1: Создание дерева директорий

    Внутри этой функции нужно написать код, который создает в папке
    `tasks/data_for_task_1` следующую структуру директорий:
    `media/images/icons/`.
    """
    path = os.path.join("tasks", "data_for_task_1", "media", "images", "icons")
    os.makedirs(path, exist_ok=True)
