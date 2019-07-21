from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

# deleting my.db clears database appropriately

# *allow for interaction with database. if it doesn't exist, 
# *create it, else load it.
# pip3 install virtualenv
# virtualenv env
# source env/bin/activate
# pip3 install flask flask-sqlalchemy
# virtualenv env?
# export FLASK_APP=app.py
# >>> from app import db
# db.create_all()
# exit()
# python3 app.py

from sqlalchemy_declarative import Images, Content, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my.db')
Base.metadata.bind = engine

# DBSession = sessionmaker()
# DBSession.bind = engine
# session = DBSession()

DBSession = sessionmaker(bind=engine)
session = DBSession()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    images = session.query(Images).all()
    content = session.query(Content).all()
    return render_template('index.html', images=images, content=content)

if __name__ == '__main__':
    app.run(debug=True)