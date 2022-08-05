test:
	docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test && flake8"

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

makemigrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations"

migrate:
	docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

superuser:
	docker-compose run --rm app sh -c "python manage.py createsuperuser"

start:
	docker-compose run --rm app sh -c "python manage.py runserver"

celery:
	docker-compose run --rm app sh -c "celery -A app worker -l INFO"

celery-clear:
	docker-compose run --rm app sh -c "celery -A app purge -f"

beat:
	docker-compose run --rm app sh -c "celery -A app beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler"
