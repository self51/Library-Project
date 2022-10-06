# **Library project**

#### About
This is a pet-project, it should not be used for commercial purposes!
<br/>A project that allows you to create a book account for the user and rent books.

##### Software that you need
* Python 3.8;
* Django 3.2;
* PostgreSQL.

##### Technology stack:
* Python 3.8, Django 3.2;
* PostgreSQL;
* HTML, CSS, Bootstrap.

##### Getting Started
* Create database in PostgreSQL.
* Add the .env file with value(SECRET_KEY, DEBUG, DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, HOST, REDIS_HOST)
* Update database settings(database and cache settings) in settings.py, if necessary.
* `$ pip install -r requirements.txt`
* `$ python manage.py makemigrations`
* `$ python manage.py migrate`
* `$ python manage.py runserver`

##### Testing application for administrators
* `$ python manage.py createsuperuser`
* Enter your desired username, email, password.
* `Username: admin`
* `Email address: admin@example.com`
* `Password: password12Q`
* `Password (again): password12Q`
* `Superuser created successfully.`

Made by `Self`.