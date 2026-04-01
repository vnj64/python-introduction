from tasks.task_3 import solve


def test_task_3():
    result = solve()

    assert isinstance(result, list), "Функция solve должна возвращать список"
    assert result == ["notes.txt", "story.txt"], f'Ожидается ["notes.txt", "story.txt"], получено {result}'
