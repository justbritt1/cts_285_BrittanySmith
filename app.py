'''
Justin Graves and Brittany Smith

'''

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

memory = 0

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    # Check if the user is not logged in
    if 'username' not in session:
        return redirect(url_for('login'))
    
    result = None

    if request.method == 'POST':
        num1 = float(request.form['num1'])
        operation = request.form['operation']
        num2 = float(request.form['num2'])

        # Perform calculation based on the selected operation
        if operation == '1':
            result = add(num1, num2)
        elif operation == '2':
            result = subtract(num1, num2)
        elif operation == '3':
            result = multiply(num1, num2)
        elif operation == '4':
            result = divide(num1, num2)
        else:
            return render_template('calculator.html', message='Invalid operation')

        # Update memory with the result
        session['memory'] = result
        
    # Handle memory recall
    memory_recall = request.args.get('memory_recall')
    if memory_recall and 'memory' in session:
        result = session['memory']

    # Pass the memory value to the template
    memory = session.get('memory', 0)

    return render_template('calculator.html', result=result, memory=memory)


@app.route('/login', methods=['GET', 'POST'])
def login():
    print("Entering login route")  # Debugging line

    if 'username' in session:
        print("User is already logged in")  # Debugging line
        return redirect(url_for('calculator'))  # Redirect to calculator if already logged in

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(f"Received login request for user: {username}")  # Debugging line

        # Replace the following line with your actual user authentication logic
        if username == 'admin' and password == 'password':
            print(f"User {username} logged in successfully.")  # Debugging line
            session['username'] = username
            return redirect(url_for('calculator'))  # Redirect to calculator on successful login
        else:
            print("Invalid credentials")  # Debugging line
            return render_template('login.html', message='Invalid credentials')

    return render_template('login.html', message='')

@app.route('/')
def index():
    return redirect(url_for('login')) # Redirect to login page

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)