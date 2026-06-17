from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/facilities.html')
def facilities():
    return render_template('facilities.html')

@app.route('/rooms.html')
def rooms():
    return render_template('rooms.html')

@app.route('/mess.html')
def mess():
    return render_template('mess.html')

@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
