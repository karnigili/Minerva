# all the imports

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import generate_password_hash

from .kanban_db_init import tasks, users

from faker import Faker
import os
import numpy as np

from . import app, db, bcrypt, login_manager

from flask_login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user, current_user


# tasks progress todo->doing->done->gone
PROG = {'todo':'doing', 'doing':'done','done':'gone'}

# login mgmt 
@login_manager.user_loader
def get_user(user_id):
    #Given uid return the associated User object.
     
    return db.session.query(users).filter(users.user_id == int(user_id)).first()

@app.route('/example')
def example():
    return ('hi')

# index page
@app.route('/')
def home():
    # redirect user to board if logged in and to login page if not
    
    # current user = logged in user
    if current_user.get_id() is None:
        return redirect(url_for('login'))

    else:
        return redirect(url_for('show_board'))


# kanban board
@login_required
@app.route('/board', methods=['GET'])
def show_board():
   
    uid = current_user.get_id()

    if uid is None:
        # abort(403, 'login')
        return redirect(url_for('home'))

    # retrieve task list and user name
    tasks_list = db.session.query(tasks.task_id, tasks.title, tasks.description, tasks.status).filter(tasks.userid == uid).all()
    user_name = db.session.query(users.username).filter(users.user_id == uid ).first()[0]
    
    todos = []
    doings = []
    dones = []

    # divide to task types
    if tasks_list is not None:

        for task in tasks_list:
            if task.status == "todo":
                todos.append(task)

            if task.status == "doing":
                doings.append(task)

            if task.status == "done":
                dones.append(task)



    return render_template('kanban.html', todos=todos, doings=doings, dones=dones, username = user_name, state_mapping=PROG)


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        if not 'password' in request.form or not 'email' in request.form or not 'username' in request.form:
            # abort(400, 'invalid input')
            return render_template('signup.html', error_msg ='please fill in all required information' )

        uname = request.form['username']
        passwd = request.form['password']
        mail = request.form['email']

        # check uname avalibility 
        try: 
            uid = db.session.query(users.user_id).\
            filter(users.username == uname).first()
            if uid is not None:

                return render_template('signup.html', error_msg ='Username is taken' )

        except:

            pass

        #adding user to the db
        add_user = users( username = uname, email = mail, password = generate_password_hash(passwd))
        db.session.add(add_user)
        db.session.commit()

        return redirect(url_for('login'))

    elif request.method == 'GET':
            return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():


    if request.method == 'POST':
        uname = request.form['username']
        candidate_pswd = request.form['password']
        
        # look for user name 
        try: 
            uid, passwd = db.session.query(users.user_id, users.password).\
            filter(users.username == uname).first()

        except :
            return render_template('login.html', error_msg ='user name does not exists' )

       
        if  uid != None:
            check_pass = bcrypt.check_password_hash(passwd, candidate_pswd.encode('utf-8'))

            if check_pass:
                login_user(get_user(uid))
                return redirect(url_for('show_board'))

            else:
                return render_template('login.html', error_msg ='wrong password' )
            

    elif request.method == 'GET':
        return render_template('login.html')

@login_required
@app.route('/tasks', methods=['POST'])
def add_task():

    task = request.form['task']
    desc = request.form.get('desc') 
    uid = current_user.get_id() 

    add_task = tasks(userid= uid, title= task, description= desc, status = 'todo')
 
    db.session.add(add_task)
    db.session.commit()

    # flash('New task was successfully posted')
    return redirect(url_for('show_board'))

@login_required
@app.route('/move_task/<task_id>', methods=['POST'])
def move_task(task_id):

    next_step = request.form['next_step']

    db.session.query(tasks).\
       filter(tasks.task_id == task_id).\
       update({tasks.status:next_step})

    db.session.commit()

    return redirect(url_for('show_board'))

@login_required
@app.route('/del_tasks/<task_id>', methods=['POST'])
def delete_task(task_id):

    db.session.query(tasks).\
       filter(tasks.task_id == task_id).\
       update({tasks.status:'gone'})

    db.session.commit()

    return redirect(url_for('show_board'))




