from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('base.html')

@app.route("/blog-feed")
def blog_feed():
    blogs = get_all_blogs()
    return render_template("blog-feed.html", blogs=blogs)

@app.route("/view-blog/{blog_id}")
def view_blog(blog_id):
    blog = get_blog(blog_id)
    return render_template("blog.html", blog=blog)

@app.route("/create-blog", methods = ['POST'])
def create_blog():
    blog_id = gen_id()
    ts = datetime.datetime.now()
    title = request.form["title"]
    desc = request.form["desc"]
    content = request.form["content"]
    blog = create_blog_as_json(blog_id, ts, title, desc, content)
    
    return render_template(f"blog.html", blog=blog)

def create_blog_as_json(blog_id, ts, title, desc, content):
    pass

def gen_id():
    id = len(get_all_blogs())
    return id

def get_blog(id):
    blogs = get_all_blogs()
    for blog in blogs:
        if blog.id == id:
            return blog
    return None

def get_all_blogs():
    blogs = ""
    return blogs