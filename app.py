from flask import Flask, render_template
import os
import json

app = Flask(__name__)
# links = {'Home':"/", 'Blog':"/blog", 'Wtf?':"/wtf"}

@app.route("/")
def main():
    return render_template('blog-form.html')

@app.route("/blog")
def blog():
    posts = get_blog_posts()
    return render_template('blog-feed.html', posts=posts)

@app.route("/wtf")
def wtf():
    return render_template('wtf.html')

@app.route("/blog/<int:blog_id>")
def blog_post(blog_id):
    posts = get_blog_posts()
    for post in posts:
        id = int(post['id'])
        if id == blog_id:
            return render_template(f'blog-post.html', post=post)
    return "Blog ain't here, man."

def get_blog_posts():
    posts = []
    posts_directory = os.path.join(app.root_path, 'posts')
    for filename in os.listdir(posts_directory):
        if filename.endswith('.json'):
            with open(os.path.join(posts_directory, filename), 'r') as file:
                post_data = json.load(file)
                posts.append(post_data)
    return posts
