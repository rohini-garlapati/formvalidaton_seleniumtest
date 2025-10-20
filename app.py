from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    year = request.form['year']

    error_name = error_email = error_password = None

    # Validations
    if not name:
        error_name = "Name cannot be empty"
    elif len(name) < 3:
        error_name = "Name must be at least 3 characters long"

    if not email:
        error_email = "Email cannot be empty"

    if not password:
        error_password = "Password cannot be empty"
    elif len(password) < 6:
        error_password = "Password must be at least 6 characters long"

    # If any errors exist, reload form with messages
    if error_name or error_email or error_password:
        return render_template(
            'form.html',
            error_name=error_name,
            error_email=error_email,
            error_password=error_password,
            request=request
        )

    # If validation passes, go to result page
    return render_template('res.html', name=name, email=email, year=year)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
