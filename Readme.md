#Usage
*First install Flask and the necessary packages* <br>
```
sudo pip install virtualenv
$ mkdir ClikUR210
$ cd ClikUR210
$ mkdir flask-workbench
$ cd flask-workbench
$ virtualenv --python=python2.7 flaskenv
$ source flaskenv/bin/activate

pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Session
pip install flask-login
pip install Flask-WTF
```
<br>
*To create the database and all that (activate the flask virtualenv first)*
```
python db_create.py
```
<br>
*Everytime major changes done to the database model*
```
python db_migrate.py
```
<br>
*To run the whole app*
```
python run.py
```
#Implementation
We used Flask, a micro-webframework based on Python, as the web framework.
The quiz creation and the question creation is/will be done in ajax.
<br>
#Files
  -/app
  1. models.py
  2. views.py
  3. forms.py
  4. __init__.py
  5. /static
  6. /template
