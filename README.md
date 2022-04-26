# Requirement

* linux based os
* python >= 3.7 and pip

# how to run project
* clone project and cd to project directory
* create and edit `.env` file based on `sample.env`
* install requirement packages via `pip install -r requirement.txt`
* migrate database via `python manage.py makemigrations`
* migrate database via `python manage.py migrate`
* create superuser via `python manage.py createsuperuser`
* run server via `python manage.py runserver 0.0.0.0:8080`

# how to run celery
* run celery via `celery -A miare worker -l info `
* run django celery beat via ` celery -A miare beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler `


 
