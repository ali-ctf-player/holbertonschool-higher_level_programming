#!/usr/bin/python3
"""IT is doc string"""

from flask import render_template, Flask

app = Flask(__name__)

@app.route("/")
def home():
    """Render template"""
    return render_template("index.html")

@app.route("/about")
def about():
    """Render template"""
    return render_template("about.html")

@app.route("/contact")
def contact():
    """Render template"""
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
