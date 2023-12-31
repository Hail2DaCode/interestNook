from flask_app import app
from flask_app.controllers import users, posts, likes, comments

app.register_blueprint(likes.likes_bp)


# ...server.py
#app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)