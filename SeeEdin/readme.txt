Team Transporter - Read Me


What is it?
—————
SeeEdin is a website designed for users to be able to quickly and easily navigate around Edinburgh in order to see its best attractions. It is still in the early stages of its development. The website uses sqlite3 and is coded in Python using the django web-framework.

Code structure
———————
templates directory holds all utilized html files for the homepage, app, etc. It also includes authentication pages.
For further detail on models and views please see the report SeeEdin.pdf

Database
—————
The structure of the database is determined from the models.py file. The database.py file holds models that
have been generated for you. If you wish to wipe the database and restart from the beginning using ‘python manage.py flush’ from terminal.
database.py is called in the views.py folder in line 18. Uncomment this code (database.add_stop(), database.add_attractions()) to add the new data and sync using ‘python manage.py syncdb’.

It is not necessary to uncomment database.add_data() except to see how Departures and BusStops are stored.

Operating instructions
——————————————
After running the app using python manage.py runserver, open up a browser and enter in to the url http://127.0.0.1:8000/. After signing up to the website you are given permission to use the app.
Click the App link and select your current destination as well as your desired destination. Click the Find a Journey button.
Currently, "Find a Journey" directs you to a page using predefined test data. This is still in the works. For further details,
please see the end of the report SeeEdin.pdf


Installation on dice instructions
——————————
Create a virtual environment:
	virtualenv -p /usr/bin/python2.7 <name of your virtual environment>

Activate:
	source <name of your virtual environment>/bin/activate

Install the modules specified in the requirements.txt file

Run the website:
	python manage.py runserver