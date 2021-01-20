# Zadaća 15.2

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project_hairdresser")
def project_hairdresser():
    return render_template("project_hairdresser.html")

@app.route("/project_fakelogin")
def project_fakelogin():
    return render_template("project_fakelogin.html")

@app.route("/project_googlehome")
def project_googlehome():
    return render_template("project_googlehome.html")

@app.route("/project_myblog")
def project_myblog():
    return render_template("project_myblog.html")


if __name__ == "__main__":
    app.run()

