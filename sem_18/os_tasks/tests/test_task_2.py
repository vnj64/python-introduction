import os
import pytest
from tasks.task_2 import solve

def test_task_2():
    data_folder = os.path.join('tasks', 'data_for_task_2')
    
    initial_files = os.listdir(data_folder)
    tmp_files_before = [f for f in initial_files if f.endswith('.tmp')]
    assert len(tmp_files_before) > 0, "В папке должны быть .tmp файлы для тестирования"
    
    other_files_before = [f for f in initial_files if not f.endswith('.tmp')]
    assert len(other_files_before) > 0, "В папке должны быть файлы с другими расширениями для тестирования"
    
    solve()
    
    final_files = os.listdir(data_folder)
    
    tmp_files_after = [f for f in final_files if f.endswith('.tmp')]
    assert len(tmp_files_after) == 0, f"В папке остались .tmp файлы: {tmp_files_after}"
    
    other_files_after = [f for f in final_files if not f.endswith('.tmp')]
    assert set(other_files_before) == set(other_files_after), "Файлы с другими расширениями были удалены или изменены"