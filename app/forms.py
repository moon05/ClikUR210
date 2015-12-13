from flask.ext.wtf import Form
from wtforms.fields import StringField, BooleanField, PasswordField, IntegerField
from  wtforms import validators


class RegistrationForm(Form):
	userName = StringField('Name') 
	studentid = StringField('StudentID', [validators.Length(min=8, max=8)])
	email = StringField('Email Address', [validators.Length(min=18, max=25)])
	#regex validator instead of length
	password = PasswordField('New Password',[validators.Required()])

class LoginForm(Form):
	userName = StringField('Name', [validators.Required()])
	password = PasswordField('Enter Password', [validators.Required()])
	remember_me = BooleanField('Remember me', default=False)

class CreateClassForm(Form):
	title = StringField('Title', [validators.Required()])
	semester = IntegerField('Semester', [validators.Required()])
	callsign = StringField('CallSign', [validators.Required()])
	CRN = IntegerField('CRN', [validators.Required()])
	session = StringField('Session', [validators.Required()])
	start_time = StringField('Start Time', [validators.Required()])
	end_time = StringField('End Time', [validators.Required()])

class CreateQuizForm(Form):
	quizName = StringField('Quiz Name', [validators.Required()])

class CreateQuestionForm(Form):
	questionText = StringField('Question Name', [validators.Required()])

class CreateOptionForm(Form):
	option = StringField('Options', [validators.Required()])
