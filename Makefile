start: #start on linux mint
	python3 -m venv .venv
	.venv/bin/python3 -m pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt
	.venv/bin/python3 manage.py runserver


test:
	coverage run manage.py test


test_report:
	coverage report -m


lint:
	pip freeze > requirements.txt
	black .
	isort .
	autopep8 ./ --recursive --in-place -a
# autoflake --in-place --remove-all-unused-imports --remove-unused-variables -r ./


migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate


docker:
	docker build --pull --rm -f "Dockerfile" -t wss:latest "."
# docker run -p localhost:localhost wss
	docker-compose up --build 


#	python -m venv .venv
#	source .venv/Scripts/activate
#	source .venv/bin/activate
#	python -m pip install --upgrade pip
#	pip install -r requirements.txt

#   python3 manage.py collectstatic

	

# # Запуск Селери
# 	python manage.py runserver
# 	python -m celery -A storegame worker -l info -P gevent
# 	python -m celery -A storegame flower --port=5555

# # селери-бит
# 	celery -A storegame beat

# # smtp сервер
# 	python3 -m smtpd -n -c DebuggingServer localhost:1025


# # Импорт экспорт БД
# 	python manage.py dumpdata --exclude auth.permission > db.json
# 	python manage.py loaddata --exclude contenttypes> db.json

# docker:
# 	docker build --pull --rm -f "Dockerfile" -t wss:latest "."
# # docker run -p localhost:localhost wss
# 	docker-compose up --build 




# djang:
# 	pip install django
# 	django-admin startproject lesson26
# 	cd lesson29
# 	python manage.py startapp signal
# 	python manage.py makemigrations
# 	python manage.py migrate
# 	python manage.py createsuperuser
# 	python3 manage.py runserver
# 	python3 manage.py runserver localhost:8000

# 	python manage.py dumpdata --exclude auth.permission > db.json
# 	python manage.py loaddata --exclude contenttypes> db.json




# ###############################################################################





# # Я попробую исправить твой код согласно рекомендациям по написанию Makefile1. Вот моя версия:

# # Define the default compiler and linker
# CC ?= gcc
# LD ?= gcc

# # Define the targets for each command
# start: venv
# .venv/bin/python3 manage.py runserver

# lint:
# pip freeze > requirements.txt
# black .
# isort .
# autopep8 ./ --recursive --in-place -a

# migrate: venv
# .venv/bin/python3 manage.py makemigrations
# .venv/bin/python3 manage.py migrate

# # Create a virtual environment and install the dependencies
# venv:
# python3 -m venv .venv
# .venv/bin/python3 -m pip install --upgrade pip
# .venv/bin/pip install -r requirements.txt

# # Clean up the virtual environment and other generated files
# clean:
# rm -rf .venv
# rm -f db.json

# .PHONY: start lint migrate venv clean

# # Вот что я изменил:

# # •  Я добавил комментарии для пояснения каждого блока кода и улучшения читаемости.

# # •  Я удалил все закомментированные строки, так как они не нужны и засоряют файл.

# # •  Я удалил лишние команды, которые не используются в приложении (celery, flower, smtp, docker).

# # •  Я вынес создание виртуального окружения в отдельный таргет и добавил его как зависимость для start и migrate таргетов.

# # •  Я добавил таргет clean для удаления виртуального окружения и других сгенерированных файлов.

# # •  Я добавил специальный таргет .PHONY для указания тех таргетов, которые не соответствуют файлам.

# # Надеюсь, это поможет тебе сделать твой код более эффективным и согласованным.blush