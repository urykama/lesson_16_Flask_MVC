from flask import Flask
from config import Config
# from head_hanter.forms_hh import HeadHunterForm
from head_hanter.statistics import Statistics

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# создания простого скрипта инициализации нашего пакета app

app = Flask(__name__)
# у нас есть конфиг, и мы должны сказать Flask'у прочесть и использовать его.
app.config.from_object(Config)
# form = HeadHunterForm()
stat = Statistics()


# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
from app import routes

# from app import views_002
# from app import views_003

# Скрипт выше просто создает объект приложения (наследуя Flask),
# затем импортирует модуль представлений, (файл  app/routes.py)
