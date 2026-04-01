from tasks.task_5 import solve


def test_task_5():
    result = solve()

    assert isinstance(result, str), "Функция solve должна возвращать строку"
    assert result == "large.txt", f'Ожидается "large.txt", получено {result}'
