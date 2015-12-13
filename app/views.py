from flask import Response, make_response
from flask import render_template, flash, redirect, url_for, request, jsonify, session, g, abort
from app import app, db, lm
from flask_security import auth_token_required
from flask_security import Security, UserMixin, RoleMixin
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, RegistrationForm, CreateClassForm
from .models import User, Allclass, Enrollment
# from .models import Quiz, MC_Question, MC_Question_Answer, MC_Question_Options
import json
import ast
import inspect
import uuid
from datetime import date, datetime, time, timedelta


@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

	
@app.before_request
def before_request():
	g.user = current_user



######   API CALLS    #######

##find all users
@app.route('/api/v1/find/users', methods=['GET'])
def find_user():
	show_users = User.query.all()
	
	converted = map(User.to_json, show_users)
	return json.dumps(converted)	

##get_user with email is DONE
@app.route('/api/v1/users/', methods=['GET'])
def get_user():
	json_data = request.json
	email_user = json_data['EMAIL']
	print email_user
	if email_user == None:
		users = User.query.all()
		converted = map(User.to_json, users)
	else:
		users = User.query.filter_by(email=email_user).first()
		# converted = map(User.to_json, users)
	# return json.dumps(converted)
	return jsonify({'userName':users.userName,'studentid':users.studentid,
					'email':users.email,'password':users.password,
					'isProfessor':users.isProfessor})




##post_user with details is DONE
##post_user for Professors with None as studentid DONE
##returns success/no success depending on creation of user
@app.route('/api/v1/users/new', methods=['POST'])
def post_user():

	json_data = request.json
	user = User(userName=json_data['NAME'],studentid=json_data['ID'],
				email=json_data['EMAIL'],password=json_data['PASS'],
				isProfessor=json_data['PROF'])
	
	try:
		db.session.add(user)
		db.session.commit()
		status = 'success'
	except:
		status = 'no success'
	db.session.close()

	return jsonify({'result':status})




##login_user WORKS return token
@app.route('/api/v1/login', methods=['GET','POST'])
def login_user():
	# data = request.data
	# data_dict = ast.literal_eval(data)
	json_data = request.json
	user = User.query.filter_by(email=json_data['EMAIL']).first()
	if user and (user.password == json_data['PASS']):
		session['logged_in'] = True
		user_token = uuid.uuid4()
		user.session_token = str(user_token)
		db.session.commit()
		curr_time = datetime.now()
		expr_time = datetime.now() + timedelta(hours=1)

		session.permanent = True
		app.permanent_session_lifetime = timedelta(hours=1)
		print user.userName
		print user.isProfessor
		print user_token
		
		status = True

		return jsonify({'result':status,'isProfessor':user.isProfessor,'token':user_token})

	else:
		status = False
		return jsonify({'result':status})



##logout_user with login token WORKS
@app.route('/api/v1/logout', methods=['POST'])
def logout_user():
	json_data = request.json
	userToken = json_data['TOKEN']
	Curr_users = User.query.filter_by(session_token=userToken)

	Curr_users.session_token = None
	db.session.commit()

	return jsonify({'result': 'logged_out'})



#get_classes with login token WORKS
@app.route('/api/v1/classes', methods=['GET','POST'])
def get_classes():
	json_data = request.json
	userToken = json_data["TOKEN"]
	# print userToken
	Curr_users = User.query.filter_by(session_token=userToken).first()
	show_classes = Curr_users.enrolled
	# print show_classes
	converted = map(Allclass.to_json, show_classes)
	return json.dumps(converted)


@app.route('/api/v1/testclasses/<token>', methods=['GET'])
def test_classes(token):
	
	Curr_users = User.query.filter_by(session_token=token).first()
	show_classes = Curr_users.enrolled
	converted = map(Allclass.to_json, show_classes)

	return json.dumps(converted)
	# return jsonify({'title':Curr_users.enrolled.Allclass.title})





##find_classes DONE without any parameters
@app.route('/api/v1/find/classes',methods=['GET'])
def find_classes():
	show_classes = Allclass.query.all()
	converted = map(Allclass.to_json, show_classes)

	return json.dumps(converted)

	# return jsonify({'title':show_classes.title,'semester':show_classes.semester,
	# 				'callsign':show_classes.callsign, 'CRN':show_classes.CRN,
	# 				'session':show_classes.session, 'start_time': show_classes.start_time,
	# 				'end_time':show_classes.end_time})



#post_class WORKS without the only professor logic
@app.route('/api/v1/classes/new', methods=['POST'])
def post_class():
	json_data = request.json
	# print data_dict
	userToken = json_data['TOKEN']
	classes = Allclass(title=json_data['TITLE'],semester=json_data['SEMESTER'],
						callsign=json_data['CALLSIGN'],CRN=json_data['CRN'],session=json_data['SESSION'],
						start_time=json_data['start_time'],end_time=json_data['end_time'])
	
	Curr_users = User.query.filter_by(session_token=userToken).first()
	classes.users.append(Curr_users)
	db.session.add(classes)
	db.session.commit()
	return jsonify({'result':'success','title':classes.title})
	# else:
	# 	return jsonify({'result':'no success'})

@app.route('/api/v1/classes/quiz/new')
def post_question():
	#gets json data
	json_data = request.json
	#
	userToken = json_data['TOKEN']
	classCRN = json_data['CRN']
	activeQuestion = json_data['ACTIVEQ']
	questionText = json_data['TEXT']
	options = json_data['CHOICES']
	optionsList = options.split('|')
	answer = json_data['ANSWER']
	Curr_users = User.query.filter_by(session_token=userToken).first()
	Curr_class = Curr_class.enrolled.filter_by(CRN=classCRN).first()
	Curr_class_id = Curr_class.id
	
	post_Options = MC_Question_Options(questionID=questionNumber,description=whatever)
	post_Question = MC_Question()
	post_Quiz = Quiz()





