from flask import Flask, render_template, request
import datetime
import random
import json
import os

app = Flask(__name__)

BLOGS_FILE = "blogs.json"
IMAGES_DIR = "static/images"

@app.route("/")
def main():
    return render_template('base.html')

@app.route("/blog-feed")
def blog_feed():
    blogs = get_all_blogs()
    return render_template("blog-feed.html", blogs=blogs)

@app.route("/view-blog/<blog_id>")
def view_blog(blog_id):
    blog = get_blog(blog_id)
    if blog:
        return render_template("blog.html", blog=blog)
    else:
        return "Blog not found", 404

@app.route("/create-blog", methods = ['POST'])
def create_blog():
    blog_id = gen_id()
    ts = datetime.datetime.now().strftime("%d/%m/%Y")
    title = request.form["title"]
    desc = request.form["desc"]
    content = request.form["content"]
    image = request.files.get("image")
    image_path = save_image(image, blog_id)

    blog = {
        "title": title,
        "id": blog_id,
        "description": desc,
        "content": content,
        "image_path": image_path,
        "date": ts  
    }    
    save_blog(blog)
    

    return render_template(f"blog.html", blog=blog)

def save_image(image, blog_id):
    mime_type = image.content_type
    file_ext = mime_type.split('/')[1]
    filename = f"{blog_id}.{file_ext}"
    image_path = os.path.join(IMAGES_DIR, filename)
    image.save(image_path)

    return image_path

def save_blog(blog):
    with open(BLOGS_FILE, 'r') as f:
        blogs = json.load(f)
    
    blogs.append(blog)
    
    with open(BLOGS_FILE, 'w') as f:
        json.dump(blogs, f, indent=4)

def gen_id():
    id = ''
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in range(4):
        id += random.choice(chars)
    return id

def get_blog(id):
    blogs = get_all_blogs()
    for blog in blogs:
        if blog['id'] == id:
            return blog
    return None

def get_all_blogs():
    with open(BLOGS_FILE, 'r') as f:
        return json.load(f)