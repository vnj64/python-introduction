from tasks.task_1 import solve


def test_task_1():
    result = solve()
    assert result == "exists", f'Ожидается строка "exists", получено {result}'
