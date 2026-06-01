import sqlite3

from flask import Flask, render_template, request, redirect
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "my_secret_key"

conn = sqlite3.connect("jobs.db", check_same_thread=False)
db = conn.cursor()

db.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    company TEXT NOT NULL,
    position TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

conn.commit()

db.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

conn.commit()


@app.route("/")
def index():

    if "user_id" not in session:
        return redirect("/login")

    db.execute(
        "SELECT * FROM jobs WHERE user_id = ?",
        (session["user_id"],)
    )

    jobs = db.fetchall()

    return render_template("index.html", jobs=jobs)

@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        company = request.form.get("company")
        position = request.form.get("position")
        status = request.form.get("status")

        db.execute(
        "INSERT INTO jobs (user_id, company, position, status) VALUES (?, ?, ?, ?)",
        (session["user_id"], company, position, status)
    )

        conn.commit()

        return redirect("/")

    return render_template("add.html")

@app.route("/delete/<int:job_id>", methods=["POST"])
def delete(job_id):

    db.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    conn.commit()

    return redirect("/")

@app.route("/edit/<int:job_id>", methods=["GET", "POST"])
def edit(job_id):

    if request.method == "POST":

        company = request.form.get("company")
        position = request.form.get("position")
        status = request.form.get("status")

        db.execute(
            "UPDATE jobs SET company = ?, position = ?, status = ? WHERE id = ?",
            (company, position, status, job_id)
        )

        conn.commit()

        return redirect("/")

    db.execute("SELECT * FROM jobs WHERE id = ?", (job_id,))
    job = db.fetchone()

    return render_template("edit.html", job=job)

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        hash_password = generate_password_hash(password)

        db.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hash_password)
        )

        conn.commit()

        return redirect("/")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        db.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = db.fetchone()

        if user and check_password_hash(user[2], password):

            session["user_id"] = user[0]

            return redirect("/")

    return render_template("login.html")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")
