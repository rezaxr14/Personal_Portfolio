# Reza Nadimi - Personal Portfolio
#### Video Demo:  https://youtu.be/a5pGDbhHg6M
#### Description: This is the source code for my personal portfolio website, submitted as my capstone project. It is a fully functional, database-driven web application built from the ground up using Python and the Flask web framework. The site showcases my engineering projects and academic achievements while demonstrating my proficiency in modern full-stack web development.

---

## 📸 Screenshots


| Homepage                                | Projects & Skills Page                      | About Page                                  |
| --------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| ![Homepage Screenshot](https://github.com/rezaxr14/Personal_Portfolio/blob/main/screenshots/Screenshot%202025-08-07%20182149.png) | ![Projects Page Screenshot](https://github.com/rezaxr14/Personal_Portfolio/blob/main/screenshots/Screenshot%202025-08-07%20182223.png)| ![About Page Screenshot](https://github.com/rezaxr14/Personal_Portfolio/blob/main/screenshots/Screenshot%202025-08-07%20182258.png)   |

---

## ✨ Features

This portfolio is more than just a static site. It includes a range of dynamic features demonstrating full-stack capabilities.

#### **Frontend & UI**
* **Fully Responsive Design:** Built with Bootstrap 5 to ensure a seamless experience on all devices, from mobile phones to desktops.
* **Modern & Clean UI:** A professional and intuitive user interface designed to be easily navigable.
* **Multi-Page Structure:**
    * **Home:** A welcoming landing page with a summary of key highlights.
    * **About Me:** A detailed section describing my background, passions, and core interests in robotics, AI, and control systems.
    * **Education & Achievements:** A timeline-style page showcasing my academic background (Sharif & Tabriz Universities), high GPA, and notable accomplishments like the Iran Mechanical Engineering Olympiad and CS50 certifications.
    * **Projects & Skills:** A dedicated page to display featured engineering projects and a categorized list of technical skills.
    * **Contact:** A page with a functional contact form for user engagement.

#### **Backend & Dynamic Functionality**
* **Flask Web Server:** The entire application is powered by a robust backend server built with Flask.
* **SQLite Database Integration:** Uses SQLite via the Flask-SQLAlchemy extension for data persistence.
* **Dual-Function Contact Form:**
    1.  **Database Storage:** All messages sent through the contact form are securely saved to the SQLite database with timestamps.
    2.  **Email Notification:** The application automatically sends a notification email to the admin (me) with the message contents upon successful submission.
* **Secure Admin Panel:**
    * **Authentication System:** A private, secure admin area protected by a username and password login system.
    * **Session Management:** Uses Flask's secure sessions to manage login state.
    * **Protected Routes:** The admin panel is inaccessible without a successful login.
    * **Message Viewer:** A sophisticated, table-based view for the admin to read all contact messages retrieved from the database, sorted by most recent.
* **Discreet Login:** The login page URL is not publicly visible in the navigation, adding a layer of security through obscurity.

---

## 🛠️ Technology Stack

This project leverages a modern stack of technologies for both backend and frontend development.

* **Backend:**
    * ![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
    * ![Flask](https://img.shields.io/badge/Flask-2.3+-black?logo=flask&logoColor=white)
    * ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-green?logo=sqlalchemy&logoColor=white)
    * ![Flask-WTF](https://img.shields.io/badge/Flask--WTF-forms-red)
    * ![Flask-Mail](https://img.shields.io/badge/Flask--Mail-emailing-orange)
* **Database:**
    * ![SQLite](https://img.shields.io/badge/SQLite-blue?logo=sqlite&logoColor=white)
* **Frontend:**
    * ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
    * ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
    * ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)
    * ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=white)

---

## 🚀 Setup and Installation

To run this project locally, please follow these steps.

#### **1. Prerequisites**
* Python 3.8+
* `pip` package manager
* A virtual environment tool (`venv` is recommended)

#### **2. Clone the Repository**
```bash
git clone [https://github.com/rezaxr14/Personal_Portfolio.git](https://github.com/rezaxr14/Personal_Portfolio.git)
cd Personal_Portfolio
```

#### **3. Create and Activate a Virtual Environment**
* **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
* **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

#### **4. Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **5. Configure Environment Variables**
This application requires environment variables for secure configuration. Create a `.env` file in the root directory and add the following:
```
SECRET_KEY="a-very-long-and-random-string-for-security"
EMAIL_USER="your.email@gmail.com"
EMAIL_PASS="your_16_character_app_password"
```

#### **6. Initialize the Database**
Before running the app for the first time, you must create the database schema. Run the following commands in your terminal:
```bash
# Start the Python interpreter
python

# Inside the Python shell, run these commands
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
...
>>> exit()
```
This will create a `messages.db` file in your project directory.

---

## 🏃‍♂️ Usage

Once the setup and configuration are complete, you can run the application.

1.  **Start the Flask Server:**
    ```bash
    python app.py
    ```
2.  **Access the Website:**
    Open your web browser and navigate to `http://127.0.0.1:5000`.

3.  **Access the Admin Panel:**
    * Navigate to `http://127.0.0.1:5000/login`.
    * Enter the admin credentials defined in `app.py` (default: `admin` / `password123`).
    * Upon successful login, you will be redirected to the `/admin/messages` page.

---

## 📁 Project Structure

```
Personal_Portfolio/
│
├── app.py              # Main Flask application logic, routes, and config
├── forms.py            # WTForms class definitions
├── messages.db         # SQLite database file
├── README.md           # This file
├── requirements.txt    # List of Python dependencies
│
├── static/             # Contains all static files
│   └── ...
│
└── templates/          # Contains all Jinja2 HTML templates
    └── ...
```

---

## 🔮 Future Improvements

While this project is fully functional, there is always room for growth. Potential future enhancements include:
* **Dynamic Project Management:** Migrating the hardcoded projects into the database and building a full CRUD interface in the admin panel.
* **Individual Project Pages:** Creating detailed pages for each project with image galleries and technical specs.
* **Blog/Updates Section:** Adding a blog to share updates on research or new skills learned.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 👨‍💻 Author

* **Reza Nadimi**
* **GitHub:** [https://github.com/rezaxr14/Personal_Portfolio](https://github.com/rezaxr14/Personal_Portfolio)
