from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import db
from app import login

grupos = db.Table('grupos', 
	db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
	db.Column('grupo_id', db.Integer, db.ForeignKey('grupo.id'), primary_key=True)
)

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	email = db.Column(db.String(120), index=True, unique=True)
	itens = db.relationship('Item', backref='author', lazy='dynamic')
	grupos = db.relationship('Grupo', secondary=grupos, 
		backref=db.backref('membros'))
	
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
		
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	
	def __repr__(self):
		return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class Item(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	itemname = db.Column(db.String(140))
	price = db.Column(db.String(10))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __repr__(self):
		return '<Post {}>'.format(self.itemname)

class Grupo(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(140))
	
