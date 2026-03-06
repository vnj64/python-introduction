# PR Review Platform (Flask)

Мини-платформа для преподавателя и студентов:
- регистрация без подтверждения email;
- роли `student` и `teacher`;
- студент отправляет ссылку на Pull Request / Merge Request;
- преподаватель видит список работ, переходит в карточку и ставит оценку (0-100) и комментарий.

## Запуск

```bash
cd pr_review_platform
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

После запуска откройте `http://127.0.0.1:5000`.

## Примечания

- База данных SQLite создается автоматически: `app.db`.
- Для продакшена нужно заменить `SECRET_KEY` и добавить полноценную авторизацию/аудит.
