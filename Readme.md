First install Flask and the necessary packages <br>
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
To create the database and all that (activate the flask virtualenv first)
```
python db_create.py
```
<br>
Everytime major changes done to the database model
```
python db_migrate.py
```
