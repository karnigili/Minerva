from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from faker import Faker
import os
import numpy as np
from . import db, bcrypt
from flask_login import UserMixin



# init dummy data creator
faker = Faker()

###### SET UP DB ######

# user class
class users(db.Model, UserMixin):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(100))

    def __repr__(self):
        return 'usename:{}, email:{}'.format(self.username, self.email)

    # def is_active(self):
    #     """True, as all user are active."""
    #     return True

    # def get_id(self):
    #     """Return the email address to satisfy Flask-Login's requirements."""
    #     return self.user_id

    # def is_anonymous(self):
    #     """False, as anonymous user aren't supported."""
    #     return False

# task class
class tasks(db.Model):
    __tablename__ = 'tasks'

    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String(120))
    description = db.Column(db.String(120))
    status = db.Column(db.String(6), db.CheckConstraint('status in ("todo","doing","done","gone")'))

    def __repr__(self):
        return 'userid:{}, title:{}, description:{}, status{}'.\
        format(self.userid, self.title, self.description, self.status)

### DUMMY DATA INSERT ###
def insert(n=4):
    n_user = n

    try:
        # create admin user
        gili_usr = users(username='gili', email='gili@admin.com', password=bcrypt.generate_password_hash('root')) 
        db.session.add(gili_usr)
        db.session.commit()

    except exc.IntegrityError:
        db.session.rollback()

    insert_user = [ users( username=faker.name().split()[0]+str(np.random.choice(range(1,99))), email=faker.email() , password= bcrypt.generate_password_hash(faker.password())) for i in range(n_user)] 
    db.session.add_all(insert_user)
    db.session.commit()

    # admin_id = admin_usr.user_id
    user_ids = [uid.user_id for uid in insert_user]
    n_tasks = n_user*4

    insert_tasks = [ tasks( userid= np.random.choice(user_ids), title= faker.word(), description= faker.text(), status = np.random.choice(["todo","doing","done","gone"])) for i in range(n_tasks)] 
    db.session.add_all(insert_tasks)
    db.session.commit()

    admin_tasks = [tasks( userid= admin_id, title= faker.word(), description= faker.text(), status = np.random.choice(["todo","doing","done","gone"])) for i in range(5)]
    db.session.add_all(admin_tasks)
    db.session.commit()


### INIT DB ###
def create_schema():
    if os.path.isfile('kanban.db'): 
        pass
    else:
        db.create_all()

        insert()

def init_db():
    create_schema()
    





