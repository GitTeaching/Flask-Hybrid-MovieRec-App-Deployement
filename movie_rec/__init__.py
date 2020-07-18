from flask import Flask


# Init app
app = Flask(__name__)

from movie_rec import routes
