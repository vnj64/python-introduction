import os

from tasks.task_4 import solve


def test_task_4():
    data_folder = os.path.join("tasks", "data_for_task_4")
    old_path = os.path.join(data_folder, "draft.txt")
    new_path = os.path.join(data_folder, "final.txt")

    assert os.path.exists(old_path), "До запуска должен существовать файл draft.txt"

    solve()

    assert not os.path.exists(old_path), "Файл draft.txt должен быть переименован"
    assert os.path.exists(new_path), "После запуска должен существовать файл final.txt"
