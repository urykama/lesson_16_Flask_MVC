#!flask/bin/python
# создание скрипта, который стартует веб-сервер нашего приложения.
from app import app

app.run(debug=True)

# Скрипт просто импортирует переменную app из нашего пакета app
# и вызывает метод run для того, чтобы запустить сервер.
# Помните, что переменная app — экземпляр класса Flask,
# мы создали его в (файле  app/__init__.py)
#   app = Flask(__name__)
