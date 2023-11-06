


from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from dataman_calculator import add, subtract, multiply, divide

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite as the database
app.secret_key = 'your_secret_key'
db = SQLAlchemy()
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

def init_db():
    with app.app_context():
        db.create_all()

# Initialize memory bank
memory = 0

# ... (other calculator functions)

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

# ... (other Flask routes)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)