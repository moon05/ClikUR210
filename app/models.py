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
								backref=db.backref('allEnrolled',lazy='dynamic'),
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
	Enroll = db.relationship('Allclass',
								secondary=Enrollment,
								primaryjoin=(Enrollment.c.class_id==id),
								backref=db.backref('classes',lazy='dynamic'),
								lazy='dynamic')

	def to_json(self):
		return {
			"title": self.title,
			"semester": self.semester
			}






# class Quiz(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	classID = db.Column(db.Integer, db.ForeignKey('Class.id'))
# 	activeQuestion = db.Column(db.Integer, db.ForeignKey('MC_Question.id'))

# class MC_Question(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	quizID = db.Column(db.Integer, db.ForeignKey('Quiz.id'))
# 	answer = db.Column(db.Integer, db.ForeignKey('MC_Question_Options.id'))
# 	questionText = db.Column(db.String(500), index=False, unique=False)

# class MC_Question_Answer(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	questionID = db.Column(db.Integer, db.ForeignKey('MC_Question.id'))
# 	student = db.Column(db.Integer, db.ForeignKey('User.studentid'))
# 	answer = db.Column(db.Integer, db.ForeignKey('MC_Question_Options.id'))
# 	answerTime = db.Column(db.DateTime)

# class MC_Question_Options(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	questionID = db.Column(db.Integer, db.ForeignKey('MC_Question.id'))
# 	description = db.Column(db.String(500), index=False, unique=False)


# class Post(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	body = db.Column(db.String(140))
# 	timestamp = db.Column(db.DateTime)
# 	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# 	def __repr__(self):
# 		return '<Post %r>' % (self.body)