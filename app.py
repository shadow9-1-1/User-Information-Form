from flask import Flask, render_template, request

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Form page route
@app.route('/form')
def form():
    return render_template('form.html')

# Result page route
@app.route('/result', methods=['POST'])
def result():
    full_name = request.form['fullName']
    dob = request.form['dob']  
    email = request.form['email']
    phone = request.form['phone']
    gender = request.form['gender']
    address = request.form['address']
    return render_template('result.html', full_name=full_name, dob=dob, email=email,phone=phone,gender=gender,address=address)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

