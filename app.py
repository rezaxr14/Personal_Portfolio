from dotenv import load_dotenv
load_dotenv() # This line loads the variables from the .env file

import os
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from forms import ContactForm
from datetime import datetime
from functools import wraps 

# --- CONFIGURATION ---
app = Flask(__name__)

# Secret key for CSRF protection in forms
# For production, use a long, random string.
app.config['SECRET_KEY'] = 'a-very-secret-key-that-you-should-change'

# Database Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'messages.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Mail Configuration - using Environment Variables for security
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# Get your email and password from environment variables
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

# Admin credentials (for demonstration)
# In a real app, use environment variables and hashed passwords.
app.config['ADMIN_USERNAME'] = 'admin'
app.config['ADMIN_PASSWORD'] = 'password123' # Change this to something more secure


# --- DATABASE MODEL ---
class ContactMessage(db.Model):
    """Database model for storing contact form submissions."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Message from {self.name}>'

# --- AUTHENTICATION DECORATOR ---
def login_required(f):
    """Decorator to ensure a user is logged in before accessing a page."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# --- ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handles the contact form: displays it and processes submissions."""
    form = ContactForm()
    if form.validate_on_submit():
        # --- Save message to database ---
        new_message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(new_message)
        db.session.commit()

        # --- Send email notification ---
        try:
            msg = Message(
                subject=f"New Contact Form Submission: {form.subject.data}",
                sender=('Reza Nadimi Website', app.config['MAIL_USERNAME']),
                recipients=[app.config['MAIL_USERNAME']] # Send email to yourself
            )
            msg.body = f"From: {form.name.data} <{form.email.data}>\n\n{form.message.data}"
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'There was an issue sending the email: {e}', 'danger')

        return redirect(url_for('contact'))
        
    return render_template('contact.html', form=form, email=app.config['MAIL_USERNAME'])


# NEW: Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == app.config['ADMIN_USERNAME'] and password == app.config['ADMIN_PASSWORD']:
            session['logged_in'] = True
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('admin_messages'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

#Logout Route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have successfully logged out.', 'info')
    return redirect(url_for('home'))

# Protected Admin Route
@app.route('/admin/messages')
@login_required # This decorator protects the page
def admin_messages():
    messages = ContactMessage.query.order_by(ContactMessage.timestamp.desc()).all()
    return render_template('admin_messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)