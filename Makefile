runserver:
	python meeple/manage.py runserver_plus [::]:8000

django:
	python meeple/manage.py

makemigrations:
	python meeple/manage.py makemigrations

migrate:
	python meeple/manage.py migrate

shell:
	python meeple/manage.py shell_plus

notebook:
	python meeple/manage.py shell_plus --notebook