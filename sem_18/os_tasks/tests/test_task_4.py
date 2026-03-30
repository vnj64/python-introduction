import os
import pytest
from tasks.task_4 import solve

def test_task_4():
    data_folder = os.path.join('tasks', 'data_for_task_4')
    
    result = solve()
    
    assert isinstance(result, dict), "Функция solve должна возвращать словарь"
    
    expected_keys = {'small', 'medium', 'large'}
    assert set(result.keys()) == expected_keys, f"Словарь должен содержать ключи {expected_keys}"
    
    for key, value in result.items():
        assert isinstance(value, int), f"Значение для ключа '{key}' должно быть целым числом"
    
    # Проверяем конкретные значения (на основе файлов, которые мы создали)
    # small_file.txt должен быть <= 100 байт
    # medium_file.txt должен быть > 100 и <= 1000 байт
    # large_file.txt должен быть > 1000 байт
    
    assert result['small'] >= 1, f"Ожидается как минимум 1 small файл, получено {result['small']}"
    assert result['medium'] >= 1, f"Ожидается как минимум 1 medium файл, получено {result['medium']}"
    assert result['large'] >= 1, f"Ожидается как минимум 1 large файл, получено {result['large']}"