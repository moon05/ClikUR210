from app import app
from app import db
from flask import render_template, flash, redirect, url_for, request, jsonify, session, g, abort
from passlib.apps import custom_app_context as pwd_context


Enrollment = db.Table('Enrollment',
	db.Column('student_id',db.Integer, db.ForeignKey('user.id')),
	db.Column('class_id',db.Integer, db.ForeignKey('tblAllclass.id')),
	db.Column('isAdmin',db.Boolean, index=False, unique=False)
	)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	studentid = db.Column(db.Integer,index=True, unique=True)
	userName = db.Column(db.String(255), index=False, unique=False)
	email = db.Column(db.String(255), index=False, unique=True)
	password = db.Column(db.String(255), index=False, unique=False)
	Enrolled = db.relationship('Allclass',
								secondary=Enrollment,
								backref='users',
								lazy='dynamic'
								)
	
	@property
	def is_authenticated(self):
		return True
	@property
	def is_active(self):
		return True
	@property
	def is_anonymous(self):
		return False
	def get_id(self):
		try:
			return unicode(self.id) #python 2
		except NameError:
			return str(self.id) #python 3

	def hash_password(password):
		return pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)

	def to_json(self):
		return {
			"userName": self.userName,
			"studentid": self.studentid,
			"email": self.email,
			"password":self.password

			}

	def enrolled_classes(self):
		#return Allclass.query.filter(User.allEnrolled.any(student_id=student_id).all())
		# return Allclass.query(User.allEnrolled.all())
		return User.query.join(Enrollment,(Enrollment.c.student_id == User.id).filter(
								Allclass.c.id==Enrollment.c.class_id))

	# def from_json(self, source):
	# 	if 'userName' in source:
	# 		self.userName = source['userName']
	# 	if 'studentid' in source:
	# 		self.studentid = source['studentid']
	# 	if 'email' in source:
	# 		self.email = source['email']

	# def _todo_response(todo):
	# 	return jsonify(**todo.to_json())



class Allclass(db.Model):
	__tablename__="tblAllclass"
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(225), index=False, unique=False)
	semester = db.Column(db.Integer, index=False, unique=False)
	callsign = db.Column(db.String, index=False, unique=False)
	CRN = db.Column(db.Integer, index=False, unique=False)
	session = db.Column(db.String, index=False, unique=False)
	start_time = db.Column(db.String, index=False, unique=False)
	end_time = db.Column(db.String, index=False, unique=False)



	"""Enroll = db.relationship('Allclass',
								secondary=Enrollment,
								primaryjoin=(Enrollment.c.class_id==id),
								backref=db.backref('classes',lazy='dynamic'),
								lazy='dynamic')"""
	quizzes = db.relationship('Quiz',
								backref="allclass",
								lazy="dynamic")
	def to_json(self):
		return {
			"id": self.id,
			"title": self.title,
			"semester": self.semester,
			"callsign": self.callsign,
			"crn": self.CRN,
			"session": self.session,
			"start_time": self.start_time,
			"end_time": self.end_time
			}



class Quiz(db.Model):
 	# __tablename__ = "Quiz"
	id = db.Column(db.Integer, primary_key=True)
	quizName = db.Column(db.String(500), index=False, unique=False)
	classID = db.Column(db.Integer, db.ForeignKey('tblAllclass.id'))
	questions = db.relationship('Question',
								backref="quiz",
								lazy="dynamic")
	
	def to_json(self):
		return{
			"quizID": self.id,
			"quizName": self.quizName,
			"classID": self.classID,
			# "activeQuestion": self.activeQuestion
		}


class Question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	quizID = db.Column(db.Integer, db.ForeignKey('quiz.id'))
	questionText = db.Column(db.String(500), index=False, unique=False)

	options = db.relationship('Option',
								backref="question",
								lazy="dynamic")

	def to_json(self):
		return{
			"quizID": self.quizID,
			# "answer": self.answer,
			"questionText": self.questionText
		}

class StudentAnswer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	questionID = db.Column(db.Integer, db.ForeignKey('Question.id'))
	student = db.Column(db.Integer, db.ForeignKey('User.studentid'))
	answer = db.Column(db.Integer)
	answerTime = db.Column(db.DateTime)

	def to_json(self):
		return{
			"questionID": self.questionID,
			"studentid": self.student,
			"answer": self.answer,
			"answerTime": self.answerTime
		}

class Option(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	questionID = db.Column(db.Integer, db.ForeignKey('question.id'))
	description = db.Column(db.String(500), index=False, unique=False)
	correct = db.Column(db.Integer,index=False,unique=False)

	def to_json(self):
		return{
			"questionID":self.questionID,
			"description":self.description,
			"correct":self.correct
		}
	