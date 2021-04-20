from flask import Flask
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)


@app.route('/')
def index():
    return "Posts Page"


@app.route('/post/<int:post_id>/')
def user_profile(post_id):
    return "Single Page"


if __name__ == "__main__":
    app.run()