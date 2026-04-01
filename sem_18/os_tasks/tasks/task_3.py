import os
import shutil


def solve():
    """
    Задание 3: Группировка файлов по первой букве

    В папке `tasks/data_for_task_3` лежит много файлов.
    Вам нужно сгруппировать их по первой букве имени.
    """
    folder = os.path.join("tasks", "data_for_task_3")
    items = os.listdir(folder)

    for item in items:
        source_path = os.path.join(folder, item)

        if os.path.isfile(source_path):
            first_letter = item[0].upper()
            target_folder = os.path.join(folder, first_letter)
            os.makedirs(target_folder, exist_ok=True)

            target_path = os.path.join(target_folder, item)
            shutil.move(source_path, target_path)
