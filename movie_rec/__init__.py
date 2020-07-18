from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Init app
app = Flask(__name__)


# Init database
app.config['SECRET_KEY'] = '4c99e0361905b9f941f17729187afdb9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://glfocxhfqbpjqm:b4c931244ad5c1b2c949d011f1b25e340e28de7bfd575bbfb2baa3051625209d@ec2-18-211-48-247.compute-1.amazonaws.com:5432/dd0pbif3qnnmqh'
db = SQLAlchemy(app)



from movie_rec import routes
