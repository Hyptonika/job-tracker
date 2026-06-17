Job Application Tracker

A full-stack web app for tracking job applications, built with Flask and SQLite. Users can register an account, log in, and manage their own list of job applications — adding, editing, and deleting entries, filtering by status, and searching by company or position.

Features


User registration and login with hashed passwords (Werkzeug security)
Per-user data isolation — each user only sees and can modify their own job applications
Add, edit, and delete job applications
Track status for each application: Applied, Interview, Offer, or Rejected
Filter applications by status
Search applications by company or position
At-a-glance summary counts (total jobs, and a count per status)
Notes field for additional details on each application
Responsive UI built with Bootstrap


Tech Stack


Backend: Python, Flask
Database: SQLite
Frontend: Jinja2 templates, Bootstrap, HTML/CSS
Security: Password hashing via Werkzeug, parameterized SQL queries, environment-based secret key


Getting Started

Prerequisites

Python 3.8+
pip


Installation


1. Clone the repository


bash   git clone <your-repo-url>
   cd <your-repo-folder>


2. Create and activate a virtual environment


bash   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate


3. Install dependencies


bash   pip install -r requirements.txt


4. Set up your environment variables
Create a .env file in the project root:


   SECRET_KEY=your-random-secret-key-here


5. Run the app


bash   python app.py

6. Open your browser to http://127.0.0.1:5000


Usage


Register a new account
Log in
Click + Add Job to create a new job application entry
Use the status filter buttons or the search bar to find specific applications
Edit or delete any application from its card


Project Structure

.
├── app.py              # Main Flask application and routes
├── templates/          # Jinja2 HTML templates
│   ├── layout.html
│   ├── index.html
│   ├── add.html
│   ├── edit.html
│   ├── login.html
│   └── register.html
├── requirements.txt
└── README.md

Security Notes


Passwords are hashed before storage and never stored or compared in plaintext
All SQL queries use parameterized statements to prevent SQL injection
Job edit/delete actions are scoped to the logged-in user, preventing access to other users' data
The Flask secret key is loaded from an environment variable rather than hardcoded in source


Future Improvements

Sort applications by date or company name

Author

Built by Paul as part of a portfolio project.