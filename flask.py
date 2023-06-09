from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Home Page'


@app.route('/career/')
def career():
    return 'Career Page'

@app.route('/contact/')
@app.route('/feedback/')
def feedback():
    return 'Feedback Page'


@app.route('/user/<int:id>')
def user_profile(id):
    return "Profile page of user #{}".format(id)


@app.route('/books/<string:genre>')
def books(genre):
    return "All Books in {} category".format(genre)


if __name__ == "__main__":
    app.run(debug=True)