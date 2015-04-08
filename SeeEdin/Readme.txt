Team Transporter - Read Me


What is it?
—————
AllExplore is a website designed for travel with a forum for individuals to interact and discuss places to visit. It is still in the early stages of its development. The website uses sqlite3 and is coded in Python using the django web-framework.

Code structure
———————
The DjangoProject directory is split into two directories. The first directory, DjangoProject, is the actual Python package for the project. The blog directory contains the files for the Django application development. Within blog you can find the utilised models in blog/models.py and the views in blog/views.py. admin.py is responsible for determining what power is held by the administrator.

HTML code for designing the website is stored in the templates folder at blog/templates. This is separated into multiple categories depending on the section of the website each file in concerned with. Continent html pages are stored in the corresponding continent directory. Forum and Blog pages follow the same procedure.

For further detail on models and views please see the report AllExplore.pdf

Database
—————
The structure of the database is determined from the models.py file. The database.py file holds models that have been generated for you if you wish to wipe the database and restart from the beginning using ‘python manage.py flush’ from terminal. database.py is called in the views.py folder in line 18. Uncomment this code to add the new data and sync using ‘python manage.py syncdb’.


Operating instructions
——————————————
‘Find an adventure’ brings you to relevant maps where you can choose the appropriate destination for you. After signing up to the website you are given the ability to actively contribute to discussions in the forum.


Installation instructions
——————————
Create a virtual environment:
	virtualenv -p /usr/bin/python2.7 <name of your virtual environment>

Activate:
	source <name of your virtual environment>/bin/activate

Install the modules specified in the requirements.txt file

Run the website:
	python manage.py runserver