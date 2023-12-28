run:
	docker-compose up
makemigrations:
	docker-compose run -rm django python manage.py makemigrations
migrate:
	docker-compose run -rm django python manage.py shell
test:
	docker-compose -f local.yml run --rm django pytest .
initdata:
	docker-compose run -rm django python manage.py init_employee_data