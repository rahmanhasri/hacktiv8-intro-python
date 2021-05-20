from flask import Flask, request, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hello, World!'
    return { 'message': 'Hello Pras!!!' }

@app.route('/hello')
def hello():
    return 'Hello'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)
@app.route('/post/<int:post_id>')
def show_post(post_id): # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
@app.route('/path/<path:subpath>')
def show_subpath(subpath): # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
@app.route('/article', methods=['GET', 'POST'])
def article():
    if request.method == 'POST':
        return 'article sudah ditambah'
    else:
        return { 'articles': [] }
# GET, POST, PUT, PATCH, DELETE
@app.route('/pages/<name>')
def pages(name='Fadlil'):
    return render_template('hello.html', name=name)
