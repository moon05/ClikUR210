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
  1. run.py
  2. db_create.py
  3. db_migrate.py
  3. db_upgrade.py
  4. db_downgrade.py
  5. config.py
  6. /app
    - models.py
    - views.py
    - forms.py
    - __init__.py
    - /static
      * functios.js
      * /images
      * style.css
      * jquery-2.1.4.min.js
    - /template
      * index.html
      * main.html
      * home.html
      * start.html
      * login.html
      * signup.html
      * myclasses.html
      * createclass.html
      * display_class.html
      * createQuiz.html
      * 404.html
      * _formhelpers.html
