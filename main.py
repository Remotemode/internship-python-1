from flask import Flask
from jinja2 import Environment, PackageLoader, select_autoescape
import json
from firebase import firebase

app = Flask(__name__)
firebase = firebase.FirebaseApplication("https://my-project-1511258558859-default-rtdb.europe-west1.firebasedatabase.app/", None)

env = Environment(
    loader=PackageLoader(__name__, 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


@app.route('/')
def index():
    data = firebase.get("my-project-1511258558859-default-rtdb")
    template = env.get_template('posts.html')
    res = json.loads(data)
    return template.render(data=res)


@app.route('/post/<int:post_id>/')
def user_profile(post_id):
    data = firebase.get("my-project-1511258558859-default-rtdb", post_id)
    template = env.get_template('single.html')
    return template.render(item=json.loads(data))


if __name__ == "__main__":
    app.run(debug=True)