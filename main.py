from flask import Flask, url_for, render_template
from markupsafe import escape
from flask import request


app = Flask(__name__)

menu = [{"name": "about", "url": 'about'},
        {"name": "objective", "url": 'objective'},
        {"name": "skills", "url": 'skills'}
        ]
for_obj = ['880 First Avenue', 'Davis, CA 95616', '+7 (702) 895-51-40', 'Aidar_amankeldy2004@mail.ru']
my_skills = ['🐍Python - 3 years', '☕Java - 6 months', '💻C++ - 3 months']


@app.route("/")
def home():
    print(url_for('home'))
    return render_template('home.html', title='Aydar Amangeldy', menu=menu)


@app.route("/hello")
def hello():
    print(url_for('hello'))
    return "<h2>Hello World!</h2>"


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title='About me')


@app.route("/objective")
def objective():
    print(url_for('objective'))
    return render_template('objective.html', title='My objective', menu=for_obj)


@app.route("/skills")
def skills():
    print(url_for('skills'))
    return render_template('skills.html', title='My skills', menu=my_skills)


'''
@app.route("extended")
def extended():
    return render_template('extended.html')
'''


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Login logic here"
    return "Rendering Login Form"


with app.test_request_context():
    print(url_for('home'))
    print(url_for('about', next='/'))
    print(url_for('static', filename='styles.css'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
