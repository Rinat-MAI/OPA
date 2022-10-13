from flask import Flask, redirect, render_template

app = Flask(__name__)

user_list = { 'User1': 'Puma', 'User2': 'Adidas', 'User3': 'Nike'}


@app.route('/')
def index():
    return redirect("/users", code=302)


@app.route('/users')
def users():
    return render_template("users.html")


@app.route('/user/<username>')
def check(username):
    if username in user_list.values():
        return redirect("/users", code=302)
    else:
        return render_template("404.html")


if __name__ == "__main__":
    app.run(debug = True)
    