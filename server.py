from flask_app.controllers import users, posts, likes
from flask_app import app
app.register_blueprint(likes.likes_bp)


# ...server.py
#app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
