from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Init app
app = Flask(__name__)

from movie_rec import routes
