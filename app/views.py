from flask import render_template, flash, redirect, url_for, request, jsonify, session, g, abort
from app import app, db, lm
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, RegistrationForm, CreateClassForm
from .models import User, Allclass, Enrollment
import json
import ast
import inspect


@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

	
@app.before_request
def before_request():
	g.user = current_user

@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
	db.session.rollback()
	return render_template('500.html'), 500

@app.route('/')

@app.route('/start')
def index():
	return render_template('start.html',
							title="ClikUR")



@app.route('/api/v1/users', methods=['GET'])
def get_user():
	users = User.query.all()
	converted = map(User.to_json, users)
	return json.dumps(converted)

@app.route('/api/v1/users/new', methods=['POST'])
def post_user():
	data = request.data
	data_dict = ast.literal_eval(data)
	print data_dict
	user = User(userName=data_dict['NAME'],studentid=data_dict['ID'],email=data_dict['EMAIL'],
				password=data_dict['PASS'])
	db.session.add(user)
	db.session.commit()
	return redirect(url_for('get_user'))






@app.route('/home')
@login_required
def home():
	user = g.user

	return render_template('home.html',
							title='Home',
							user=user)

@app.route('/signup',methods=['GET','POST'])
def signup():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(userName = form.userName.data, studentid = form.studentid.data,
					email = form.email.data, password = form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Thanks for registering')
		return redirect(url_for('login'))
	else:
		return render_template('signup.html', 
							title='Sign Up',
							form=form)

@app.route('/login',methods=['GET','POST'])
def login():
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		print form.userName.data
		user = User.query.filter_by(userName=form.userName.data).first()
		print user
		if user and user.password == form.password.data:
			remember = form.remember_me.data
			print remember
			user.authenticated = True
			db.session.commit()
			login_user(user, remember=remember)
			print "Login Successful"
			return redirect(url_for('home'))
	return render_template('login.html',
							title='Sign In',
							form=form)




# @oid.after_login
# def after_login(resp):
# 	if resp.email is None or resp.email == "":
# 		flash('Invalid login. Please try again')
# 		return redirect(url_for('login'))
# 	user = User.query.filter_by(email=resp.email).first()
# 	if user is None:
# 		userName = resp.userName
# 		if userName is None or userName=="":
# 			userName = resp.email.split('@')[0]
# 		user = User(userName=userName,email=resp.emai)
# 		db.session.add(user)
# 		db.session.commit()
# 	remember_me = False
# 	if 'remember_me' in session:
# 		remember_me = session['remember_me']
# 		session.pop('remember_me',None)
# 	login_user(user, remember = remember_me)
# 	return redirect(url_for('home.html'))



@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


#classes part
@app.route('/api/v1/classes', methods=['GET'])
def get_classes():
	show_classes = Allclass.query.all()
	converted = map(Allclass.to_json, show_classes)
	 
	return json.dumps(converted)

@login_required
@app.route('/myclasses',methods=['GET','POST'])
def myclasses():
	user = g.user
	print ""
	user2 = g.user
	# print "Printing user2: " + str(user2.Enroll)
	print ""
	print "Printing relationship"
	# print user.Enroll
	print "End print"
	# show_classes = user.enrolled_classes
	# print show_classes
	# converted = map(Allclass.to_json, user.Enroll)
	# return json.dumps(converted)
	return json.dumps(user.Enrolled)
	
@app.route('/api/v1/classes/new', methods=['POST'])
def post_class():
	data = request.data
	data_dict = ast.literal_eval(data)
	print data_dict
	classes = Allclass(title=data_dict['TITLE'],semester=data_dict['SEMESTER'])
	db.session.add(classes)
	db.session.commit()
	return redirect(url_for('get_classes'))



@app.route('/createclass',methods=['GET', 'POST'])
def createclass():
	form = CreateClassForm()
	if form.validate_on_submit():
		newClass = Allclass(title=form.title.data, semester=form.semester.data)
		db.session.add(newClass)
		db.session.commit()
		return redirect(url_for('myclasses'))
	else:
		return render_template('createclass.html',
								title='Create Class',
								form=form)



