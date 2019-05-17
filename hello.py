import os

from flask import Flask, flash, redirect, request, session, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "/path/to/the/uploads"
ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif"])

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    username = "Anonymous"
    if "username" in session:
        username = session["username"]
        logout_link = url_for("logout")
        return f"""
            <p>Main page</p>
            <p>You are logged in as {username}</p>
            <a href="{logout_link}">logout</a>
        """

    login_link = url_for("login")

    return f"""
        <p>Main page</p>
        <a href="{login_link}">login</a>
    """


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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return """
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    """


@app.route("/logout")
def logout():
    # remove the username from the session if it's there
    session.pop("username", None)
    return redirect(url_for("index"))


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/file/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files["file"]

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("uploaded_file", filename=filename))
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    """
