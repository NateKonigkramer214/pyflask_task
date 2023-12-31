from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/HTML/about.html')
def about():
    return render_template('about.html')

@app.route('/HTML/contact_us.html')
def contact():
    return render_template('contact_us.html')

@app.route('/HTML/shop.html')
def shop():
    return render_template('shop.html')

@app.route('/HTML/login.html')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
