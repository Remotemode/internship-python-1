from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Posts Page"


@app.route('/post/<int:post_id>/')
def user_profile(post_id):
    return "Single Page"


if __name__ == "__main__":
    app.run()