from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Init app
app = Flask(__name__)


# Init database
app.config['SECRET_KEY'] = '4c99e0361905b9f941f17729187afdb9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top_movies.db'
db = SQLAlchemy(app)



from movie_rec import routes