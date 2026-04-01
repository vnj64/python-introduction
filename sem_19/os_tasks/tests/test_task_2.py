import os

from tasks.task_2 import solve


def test_task_2():
    data_folder = os.path.join("tasks", "data_for_task_2")
    result = solve()

    assert isinstance(result, list), "Функция solve должна возвращать список"
    assert result == [3, 2], f"Ожидается [3, 2], получено {result}"
    assert os.path.isdir(data_folder), "Папка с данными должна существовать"
