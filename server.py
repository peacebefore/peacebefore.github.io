from flask import Flask, render_template
app = Flask(__name__)
print(__name__)


@app.route('/<username>')
def hello_world(username=None):
    return render_template('index.html', name=username)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    return 'These are my thoughts on blogs!'
