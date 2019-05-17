from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "Hello, World!"


@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name}!"


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    print(type(post_id))
    return f"data for {post_id}"


@app.route("/projects/")
def projects():
    return "The project page"


@app.route("/about")
def about():
    return "The about page"


@app.route("/about/")
def about2():
    return "The about page 2"
