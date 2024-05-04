from flask import Flask, render_template

app = Flask(__name__)
links = {'Home':"/", 'Blog':"/blog", 'Wtf?':"/wtf"}

@app.route("/")
def main():
    return render_template('blog-form.html', links=links)

@app.route("/blog")
def blog():
    return render_template('blog-feed.html', links=links)

@app.route("/wtf")
def wtf():
    return render_template('wtf.html', links=links)

@app.route("/blog/<int:blog_id>/<blog_title>")
def blog_post(blog_id, blog_title):
    return f"BlogID: {blog_id} - Title: {blog_title}"