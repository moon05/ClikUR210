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
  1. run.py (_contains the run information with portname, hostname and debug enabling_)
  2. db\_create.py (_script to create the database_)
  3. db\_migrate.py (_script for big upgrade of database_)
  3. db\_upgrade.py (_small upgrades_)
  4. db\_downgrade.py (_going one version back_)
  5. config.py (_contains all the locations of files_)
  6. /app
    - models.py (_database tables/models declarations_)
    - views.py (_app routing and info handling_)
    - forms.py (_contains all the necessary forms_)
    - __init__.py (_app initializer_)
    - /static
      * functions.js (_contains all the necessary .js functions_)
      * /images (_contains the logos and necessary images_)
      * style.css (_all the styling_)
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
