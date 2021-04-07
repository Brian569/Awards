serve:
	python manage.py runserver

migrations:
	python manage.py makemigrations ${app}

migrate:
	python manage.py migrate

admin:
	python manage.py createsuperuser

shell:
	python manage.py shell

check:
	python manage.py check

test:
	python manage.py test