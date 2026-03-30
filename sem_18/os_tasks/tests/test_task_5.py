import os
import pytest
from tasks.task_5 import solve

def test_task_5():
    data_folder = os.path.join('tasks', 'data_for_task_5')

    result = solve()

    assert isinstance(result, list), "Функция solve должна возвращать список"

    for item in result:
        assert isinstance(item, str), "Все элементы списка должны быть строками"

    for file_name in result:
        assert file_name.endswith('.txt'), f"Файл {file_name} не имеет расширения .txt"

    expected_files = ['notes.txt', 'report.txt']
    assert result == expected_files, f"Ожидается список {expected_files}, получено {result}"

    nested_file = os.path.join(data_folder, 'archive', 'hidden.txt')
    assert nested_file not in result, "Файл из вложенной папки не должен попадать в результат"
