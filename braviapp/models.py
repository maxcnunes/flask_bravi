from braviapp import db

class News(db.Model):
	# Define the properties mapped to database columns
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100), nullable = False)
	text = db.Column(db.Text, nullable = False)

	def __init__(self, title, text):
		self.title = title
		self.text = text

	def __repr__(self):
		return '<News %r>' % self.title
