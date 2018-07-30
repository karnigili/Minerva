Quick-start
----------
Make sure you are currently in the app directory 

Setting the environment variables
```bash
export FLASK_APP=kanban_flask.py
export FLASK_DEBUG=1
```

Activating a virtual environment
```bash	
virtualenv -p python3.6 venv
source venv/bin/activate\ 
```
Install required packages
```bash	
pip3 install -r requirements.txt
```
The DB will be initiated with the first run of the app

To run the server execute
```bash		
flask run
```

To test the app, run to following. The first line using the local tests file and the second two will run a coverage test and open a html with a test coverage report. Make sure the server is up and running before starting the tests
```bash
coverage run tests.py

coverage html
open htmlcov/index.html
```

To see your application, access this URL in your browser
```
http://localhost:5000
```



App components
----------
__init__.py
	This file initiates the app, the login manager, and the DB.

kanban_db_init.py
	This file initiates the DB. This file also consists of password encryption and user managing methods.

	The users table holds login information for each user and the tasks contains all information about the task for each user.

	This file is called when initiating the app using __init__.py thus the DB itself will be restored per app initiation.

	The DB first call creates dummy data using faker library.


kanban.db
	The schema consists of two tables; 
	users : user_id, username, email, password
	tasks :  task_id, userid, title, description, status

	The DB is an sqlite DB.

kanban_flask.py
	This is the main file of the app. Consists of all endpoints and logic of the app. 


tests.py
	Contains functionality tests for the app.
	

All static html pages are in /templates 
All html design code is consisted within the static/styles.css file.


