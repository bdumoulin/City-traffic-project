# City-traffic-project
SE Project for UTCN : City traffic software


To launch the app :

python manage.py runserver


If the DB is not available directly do :

python manage.py makemigrations & 
python manage.py migrate


Here are the pages available now :
- admin page : http://localhost:8000/admin/
- home : http://localhost:8000/traffic/
- map descriptor : http://localhost:8000/traffic/map/
- path calculator : http://localhost:8000/traffic/way/


PLEASE USE YOUR BRANCH TO MODIFY THE CODE, WHAT IS ON MAIN MUST BE WORKING !

Important files to modify : 
- model : models.py
- view : views.py
- URL : traffic_site/urls.py and traffic_app/urls.py
- HTML : templates/*.html


If you modify the model do :

python manage.py makemigrations & 
python manage.py migrate
