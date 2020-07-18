from movie_rec import db


#Movie class/model
class TopMovie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), unique=True, nullable=False)
	score = db.Column(db.Float, nullable=False)

	def __init__(self, id, title, score):
		self.id = id
		self.title = title
		self.score = score

	def __repr__(self):
		return f"Movie('{self.id}', '{self.title}')"
