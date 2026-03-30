import os
import pytest
from tasks.task_3 import solve

def test_task_3():
    data_folder = os.path.join('tasks', 'data_for_task_3')
    
    initial_files = os.listdir(data_folder)
    assert len(initial_files) > 0, "В папке должны быть файлы для тестирования"
    
    solve()
    
    final_items = os.listdir(data_folder)
    
    expected_folders = {'A', 'B', 'C', 'D', 'E'}
    actual_folders = {item for item in final_items if os.path.isdir(os.path.join(data_folder, item))}
    assert expected_folders.issubset(actual_folders), f"Не все ожидаемые папки созданы. Ожидаемые: {expected_folders}, Созданные: {actual_folders}"
    
    assert os.path.exists(os.path.join(data_folder, 'A', 'apple.txt')), "Файл apple.txt не найден в папке A"
    
    assert os.path.exists(os.path.join(data_folder, 'B', 'Bear.jpg')), "Файл Bear.jpg не найден в папке B"
    
    assert os.path.exists(os.path.join(data_folder, 'C', 'cat.png')), "Файл cat.png не найден в папке C"
    
    assert os.path.exists(os.path.join(data_folder, 'D', 'Dog.gif')), "Файл Dog.gif не найден в папке D"
    
    assert os.path.exists(os.path.join(data_folder, 'E', 'elephant.bmp')), "Файл elephant.bmp не найден в папке E"