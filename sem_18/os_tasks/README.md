### Шаг 1: Клонируйте репозиторий

Откройте терминал (или Git Bash на Windows) и выполните команду:

```bash
git clone https://github.com/vnj64/python-introduction.git
cd python-introduction/sem_18/os_tasks
```

### Шаг 2: Создайте и активируйте виртуальное окружение

```bash
# Создаем окружение в папке 'venv'
python -m venv venv

# Активируем его:
# Для Windows
venv\Scripts\activate

# Для macOS / Linux
source venv/bin/activate
```
После активации вы увидите `(venv)` в начале строки вашего терминала.

### Шаг 3: Установите `pytest`

```bash
pip install pytest
```

## ✅ Как проверить свое решение

Для каждого задания есть свой тестовый файл. Чтобы проверить конкретное задание, выполните в терминале команду:

```bash
# Для проверки Задания 1
python -m pytest tests/test_task_1.py

# Для проверки Задания 2
python -m pytest tests/test_task_2.py
```
...и так далее для остальных заданий.

Если вы хотите запустить сразу все тесты, просто выполните команду `python -m pytest` из корневой папки проекта.
