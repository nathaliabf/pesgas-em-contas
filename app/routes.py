from flask import render_template, flash, redirect, url_for
from app import app 
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
	user = {'username': 'charlottinha'}
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
	return render_template('index.html', title='Home', user=user, itens=itens)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login request for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)
