from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    
    if not username or not email or not password:
        message = "All fields are required!"
        return render_template('register.html', message=message, message_type='error')
    
    # Simulate successful registration logic here
    return redirect(url_for('home', success='true'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
