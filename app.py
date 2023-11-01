from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from dataman_calculator import add, subtract, multiply, divide
from auth import db, User, init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite as the database
app.secret_key = 'your_secret_key'
db.init_app(app)

# ... (other routes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', message='Invalid credentials')

    return render_template('login.html', message='')

# ... (other routes)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)