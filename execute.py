from flask import Flask, render_template, session, request, redirect, url_for,flash
app = Flask(__name__,template_folder='templates')
@app.route("/")
def search_index():
    return render_template("index.html")
@app.route("/search_pdf")
def search():
    return render_template("search.html")

if __name__=="__main__":
    app.debug=True
    app.run(host="127.0.0.1",port=5000)