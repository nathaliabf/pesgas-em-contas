from datetime import datetime
from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	itens = db.relationship('Item', backref='author', lazy='dynamic')
	
	def __repr__(self):
		return '<User {}>'.format(self.username)

class Item(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	itemname = db.Column(db.String(140))
	price = db.Column(db.String(10))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __repr__(self):
		return '<Post {}>'.format(self.itemname)
