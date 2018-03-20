from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import *

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remamber Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Usuario', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Senha', validators=[DataRequired()])
	password2 = PasswordField('Repetir senha', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Registrar')
	
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Escolha um nome de usuario diferente.')
			
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Esse email ja esta em uso.')		

class GroupForm(FlaskForm):
	name = StringField('Nome do grupo', validators=[DataRequired()])
	submit = SubmitField('Sign In')
	
	def validate_groupname(self, name):
		grupo = Grupo.query.filter_by(name=name.data).first()
		if grupo is not None:
			raise ValidationError('Nome do grupo em uso')
