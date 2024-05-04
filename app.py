from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    links = {'Link 1':"/slug-1", 'Link 2':"/slug-2", 'Link 3':"/slug-3"}
    return render_template('base.html', links=links)