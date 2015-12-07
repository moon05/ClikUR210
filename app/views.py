from flask import render_template, flash, redirect, url_for, request, jsonify, session, g, abort
from app import app, db, lm
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, RegistrationForm, CreateClassForm, CreateQuizForm
from .models import User, Allclass, Enrollment, Quiz, Question, Option
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
def index():
	return render_template('start.html',
							title="ClikUR")

######   API CALLS    #######


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

@app.route('/api/v1/classes', methods=['GET'])
def get_classes():
	show_classes = Allclass.query.all()
	converted = map(Allclass.to_json, show_classes)
	 
	return json.dumps(converted)

@app.route('/api/v1/classes/new', methods=['POST'])
def post_class():
	data = request.data
	data_dict = ast.literal_eval(data)
	print data_dict
	classes = Allclass(title=data_dict['TITLE'],semester=data_dict['SEMESTER'])
	classes.users.append(g.user)
	db.session.add(classes)
	db.session.commit()
	return redirect(url_for('get_classes'))


######   WEBSITE   ######


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


@login_required
@app.route('/myclasses',methods=['GET','POST'])
def myclasses():
	user = g.user
	print ""
	# print "Printing relationship" 
	# for classes in user.enrolled.all():
	# 	print classes.title
	# 	print classes.semester
	# print "End print"
	show_classes = user.Enrolled.all()
	converted = map(Allclass.to_json, show_classes)
	print "converted type: " + str(type(converted))
	print converted
	
	# list_both = []
	# for i in (converted):
	# 	list_both.append((i['title'],i['semester']))
	
	# return json.dumps(converted)
	return render_template('myclasses.html',result=converted)


@login_required
@app.route('/createclass',methods=['GET', 'POST'])
def createclass():
	form = CreateClassForm()
	if form.validate_on_submit():
		newClass = Allclass(title=form.title.data, semester=form.semester.data,
							callsign=form.callsign.data, CRN = form.CRN.data,
							session=form.session.data, start_time=form.start_time.data,
							end_time=form.end_time.data)
		newClass.users.append(g.user)
		db.session.add(newClass)
		db.session.commit()
		return redirect(url_for('myclasses'))
	else:
		return render_template('createclass.html',
								title='Create Class',
								form=form)

##to get the id of the class for adding quiz
@login_required
@app.route('/class/<class_id>',methods=['GET', 'POST'])
def display_class(class_id=None):

	myClass = Allclass.query.filter_by(id=class_id).first()

	form = CreateQuizForm()


	return render_template('display_class.html',class_obj = myClass, form=form)


#to get class info in json format
@login_required
@app.route('/class_js/<class_id>',methods=['GET', 'POST'])
def get_class_json(class_id=None):

	myClass = g.user.Enrolled.filter_by(id=class_id).first()
    
    #creating response object
	response = jsonify(myClass.to_json())
	response.status_code = 200 

	return response

@login_required
@app.route('/createQuiz',methods=['GET','POST'])
def createQuiz(class_id=None):

	form = CreateQuizForm()
	
	print request.values.to_dict()
	new_quiz = request.values.to_dict()
	print new_quiz['quizName']
	print new_quiz['class_id']
	
	if new_quiz:
		newQuiz = Quiz(quizName=new_quiz['quizName'])
		curr_class = Allclass.query.filter_by(id=new_quiz['class_id']).first()
		curr_class.quizzes.append(newQuiz)
		db.session.add(curr_class)
		db.session.commit()
		quizzes = Quiz.query.all()
		converted = map(Quiz.to_json, quizzes)
		print converted

		# converted = map(Quiz.to_json, newQuiz)
		# if everything goes right, change the status
		response = jsonify({'status':'True'})
		response.status_code = 200	
	else:
		response = jsonify({'status':'False'})
		response.status_code = 200

	return response

@login_required
@app.route('/removeQuiz', methods=['GET','POST'])
def deleteQuiz(class_id=None):
	quiz_delete = request.values.to_dict()
	print quiz_delete['quiz_id']

	if quiz_delete:
		curr_class = Allclass.query.filter_by(id=quiz_delete['class_id']).first()
		curr_class.quiz.filter_by(id=quiz_delete['quiz_id']).first().delete()
		db.session.commit()
		response = jsonify({'status':'True'})
		response.status_code = 200
	else:
		response = jsonify({'status':'False'})
		response.status_code = 200

	return response



