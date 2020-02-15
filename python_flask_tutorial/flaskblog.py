from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"

@app.route("/admin")
def admin():
    return "<h1>Admin Page!</h1>"



# use 'flask run' instead
if __name__ == '__main__':
    app.run(debug=True)
