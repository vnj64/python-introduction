from __future__ import annotations

import sqlite3
from datetime import datetime
from functools import wraps
from pathlib import Path
from urllib.parse import urlparse

from flask import Flask, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "app.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key-change-me"


# --- Database helpers ---
def get_db() -> sqlite3.Connection:
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_: object) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db() -> None:
    db = get_db()
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('student', 'teacher')),
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            pr_url TEXT NOT NULL,
            title TEXT,
            note TEXT,
            status TEXT NOT NULL DEFAULT 'submitted' CHECK(status IN ('submitted', 'reviewed')),
            score INTEGER,
            teacher_comment TEXT,
            reviewed_by INTEGER,
            reviewed_at TEXT,
            created_at TEXT NOT NULL,
            FOREIGN KEY(student_id) REFERENCES users(id),
            FOREIGN KEY(reviewed_by) REFERENCES users(id)
        );
        """
    )
    db.commit()


# --- Auth helpers ---
def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if g.user is None:
            flash("Сначала войдите в систему.", "error")
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped


def role_required(required_role: str):
    def decorator(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            if g.user is None:
                flash("Сначала войдите в систему.", "error")
                return redirect(url_for("login"))
            if g.user["role"] != required_role:
                flash("Недостаточно прав для этой страницы.", "error")
                return redirect(url_for("dashboard"))
            return view(*args, **kwargs)

        return wrapped

    return decorator


@app.before_request
def load_logged_in_user() -> None:
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
        return

    db = get_db()
    g.user = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()


@app.context_processor
def inject_now():
    return {"now": datetime.utcnow()}


# --- Utils ---
def is_valid_pr_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
    except ValueError:
        return False

    if parsed.scheme not in {"http", "https"}:
        return False

    if not parsed.netloc:
        return False

    path = parsed.path.strip("/")
    parts = path.split("/")

    # Typical GitHub/GitLab pattern: /owner/repo/pull/123 or /merge_requests/123
    if len(parts) < 4:
        return False

    markers = {"pull", "pulls", "merge_requests", "merge-requests"}
    return any(marker in parts for marker in markers)


# --- Routes ---
@app.route("/")
def index():
    if g.user:
        return redirect(url_for("dashboard"))
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        role = request.form.get("role", "student")

        error = None

        if not username:
            error = "Введите username."
        elif len(username) < 3:
            error = "Username должен быть не короче 3 символов."
        elif len(password) < 6:
            error = "Пароль должен быть не короче 6 символов."
        elif role not in {"student", "teacher"}:
            error = "Неверная роль."

        db = get_db()
        if error is None:
            existing = db.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
            if existing:
                error = "Такой username уже занят."

        if error is None:
            db.execute(
                "INSERT INTO users(username, password_hash, role, created_at) VALUES (?, ?, ?, ?)",
                (username, generate_password_hash(password), role, datetime.utcnow().isoformat()),
            )
            db.commit()
            flash("Регистрация успешна. Теперь войдите.", "success")
            return redirect(url_for("login"))

        flash(error, "error")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

        if user is None or not check_password_hash(user["password_hash"], password):
            flash("Неверный username или пароль.", "error")
            return render_template("login.html")

        session.clear()
        session["user_id"] = user["id"]
        flash("Вход выполнен.", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/logout", methods=["POST"])
@login_required
def logout():
    session.clear()
    flash("Вы вышли из системы.", "success")
    return redirect(url_for("index"))


@app.route("/dashboard")
@login_required
def dashboard():
    if g.user["role"] == "student":
        return redirect(url_for("student_dashboard"))
    return redirect(url_for("teacher_dashboard"))


@app.route("/student", methods=["GET", "POST"])
@role_required("student")
def student_dashboard():
    db = get_db()

    if request.method == "POST":
        pr_url = request.form.get("pr_url", "").strip()
        title = request.form.get("title", "").strip()
        note = request.form.get("note", "").strip()

        if not pr_url:
            flash("Добавьте ссылку на Pull Request.", "error")
        elif not is_valid_pr_url(pr_url):
            flash("Ссылка не похожа на PR/MR. Пример: github.com/.../pull/123", "error")
        else:
            db.execute(
                """
                INSERT INTO submissions(student_id, pr_url, title, note, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (g.user["id"], pr_url, title or None, note or None, datetime.utcnow().isoformat()),
            )
            db.commit()
            flash("PR отправлен на проверку.", "success")
            return redirect(url_for("student_dashboard"))

    submissions = db.execute(
        """
        SELECT s.*, t.username AS teacher_username
        FROM submissions s
        LEFT JOIN users t ON t.id = s.reviewed_by
        WHERE s.student_id = ?
        ORDER BY s.created_at DESC
        """,
        (g.user["id"],),
    ).fetchall()

    return render_template("student_dashboard.html", submissions=submissions)


@app.route("/teacher")
@role_required("teacher")
def teacher_dashboard():
    db = get_db()

    submissions = db.execute(
        """
        SELECT s.*, u.username AS student_username, t.username AS teacher_username
        FROM submissions s
        JOIN users u ON u.id = s.student_id
        LEFT JOIN users t ON t.id = s.reviewed_by
        ORDER BY
            CASE s.status WHEN 'submitted' THEN 0 ELSE 1 END,
            s.created_at DESC
        """
    ).fetchall()

    return render_template("teacher_dashboard.html", submissions=submissions)


@app.route("/teacher/review/<int:submission_id>", methods=["GET", "POST"])
@role_required("teacher")
def review_submission(submission_id: int):
    db = get_db()
    submission = db.execute(
        """
        SELECT s.*, u.username AS student_username
        FROM submissions s
        JOIN users u ON u.id = s.student_id
        WHERE s.id = ?
        """,
        (submission_id,),
    ).fetchone()

    if submission is None:
        flash("Работа не найдена.", "error")
        return redirect(url_for("teacher_dashboard"))

    if request.method == "POST":
        score_raw = request.form.get("score", "").strip()
        teacher_comment = request.form.get("teacher_comment", "").strip()

        error = None
        try:
            score = int(score_raw)
            if not (0 <= score <= 100):
                error = "Оценка должна быть от 0 до 100."
        except ValueError:
            error = "Оценка должна быть целым числом."
            score = None

        if error is None:
            db.execute(
                """
                UPDATE submissions
                SET status = 'reviewed',
                    score = ?,
                    teacher_comment = ?,
                    reviewed_by = ?,
                    reviewed_at = ?
                WHERE id = ?
                """,
                (
                    score,
                    teacher_comment or None,
                    g.user["id"],
                    datetime.utcnow().isoformat(),
                    submission_id,
                ),
            )
            db.commit()
            flash("Оценка сохранена.", "success")
            return redirect(url_for("teacher_dashboard"))

        flash(error, "error")

    return render_template("review_submission.html", submission=submission)


@app.route("/health")
def health():
    return {"ok": True}


if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)
