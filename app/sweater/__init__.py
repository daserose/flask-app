from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# settings for db (postgres)
# need to hide -user- -password-
DBUSER = 'postgres1'
DBPASS = '111'
DBHOST = 'postgres' # for docker-compose
#DBHOST = 'localhost' # for lockal run (localhost:5000)
DBPORT = '5432'
DBNAME = 'py_sweater'


app = Flask(__name__)
app.secret_key = 'some secret bitter sugar'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres1:111@localhost:15432/py_sweater'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

from sweater import modules, routes

db.create_all()
app.run(host="0.0.0.0", debug=True) #for docker-compose
#app.run(debug=True)
