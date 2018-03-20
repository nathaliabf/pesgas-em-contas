from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from app import app , db
from app.models import *
from app.forms import *
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
	itens = [
		{
			'nome': 'racao',
			'preco': '38',
			'data': '13/03'
		},
		{
			'nome': 'petisco',
			'preco': '1,70',
			'data': '13/03'
		}
	]
	return render_template('index.html', title='Home', user=current_user, itens=itens)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Usuario ou senha invalidos')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
		#return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Cadastro feito com sucexo!')
		return redirect(url_for('index'))
	return render_template('register.html', title='Registro', form=form)

@login_required
@app.route('/creategroup', methods=['GET', 'POST'])
def creategroup():
	form = GroupForm()
	if form.validate_on_submit():
		grupo = Grupo(name=name.data)
		grupo.membros.append(current_user)
		db.session.add(grupo)
		db.session.commit()
		return redirect(url_for('index')) #EVENTUALMENTE COLOCAR URL DE ADICIONAR MEMBRO
	return render_template('creategroup.html', title='Novo grupo', form=form)
	
