mig:
	python manage.py makemigrations
	python manage.py migrate

user:
	python manage.py createsuperuser

app:
	python manage.py startapp apps

