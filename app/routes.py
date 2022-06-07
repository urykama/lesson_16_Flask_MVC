from flask import render_template, flash, redirect, url_for, request
from app import app
from app import stat
from app.forms import LoginForm
from head_hanter.forms_hh import HeadHunterForm
from head_hanter.find_area_id import get_id_region
from head_hanter.parser_hh import parser


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Amigos'}  # выдуманный пользователь
    posts = [
        {
            'author': {'username': 'УНИВЕРСИТЕТ ИСКУССТВЕННОГО ИНТЕЛЛЕКТА TERRA AI'},
            'body': 'https://neural-university.ru/'
        },
        {
            'author': {'username': 'Мега-Учебник Flask, Часть 2: Шаблоны (издание 2018)'},
            'body': 'https://habr.com/ru/post/346340/'
        },
        {
            'author': {'username': 'Bootstrap 4. Быстрый старт.'},
            'body': 'https://www.youtube.com/watch?v=bmJ_Da_kZXo&list=PLD-piGJ3Dtl3_uQlbecPN945VZr11jUzG&index=7'
        }
    ]
    return render_template("index.html",
                           title='Главная страница',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, password {}, remember_me={}'.format(
            form.username.data, form.password.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/form_hh', methods=['GET', 'POST'])
def form_hh():
    form_hh = HeadHunterForm()
    if form_hh.validate_on_submit():
        city = str(form_hh.password.data).strip().capitalize()
        print('city: ', city)
        id = get_id_region(url_area='https://api.hh.ru/areas/113', val=city)
        print(id)
        search_bar = str(form_hh.search_bar.data).strip()
        print(search_bar)
        if id:
            print(12345)
            parser(stat, region_id=id, search_bar=search_bar)
            # print(stat.get_stat())
            # flash('Login requested for user {}, password {}, remember_me={}'.format(
                # form_hh.username.data, form_hh.password.data, form_hh.remember_me.data))
            return redirect(url_for('results'))
        else:
            flash('Такой город не найден {}'.format(form_hh.password.data))
    return render_template('form_hh.html', title='Form_HH', form=form_hh, submit='Войти')


@app.route('/contacts')
def contacts():
    user = {'nickname': 'Камалетдинов Урал Аданисович'}  # выдуманный пользователь
    posts = [
        {
            'author': {'username': 'Адрес'},
            'body': 'г.Уфа - Столица R@B, центр'
        },
        {
            'author': {'username': 'Телефон'},
            'body': '+79174189728'
        },
        {
            'author': {'username': 'E-mail'},
            'body': 'urykama@gmail.com'
        },
        {
            'author': {'username': 'WhatsApp'},
            'body': 'Урал Камазыч'
        },
        {
            'author': {'username': 'Телеграмм'},
            'body': 'https://t.me/Ural_Kama_AD'
        },
        {
            'author': {'username': 'Skype'},
            'body': 'Ural Kama'
        }
    ]
    print(type(posts))
    return render_template('contacts.html', title='Contacts', user=user, posts=posts)


@app.route('/results')
def results():
    # posts = [('Python', 34), ('Git', 14), ('Linux', 11), ('JavaScript', 11), ('SQL', 10), ('CSS', 9), ('PostgreSQL', 8), ('HTML', 8), ('Java', 7), ('Docker', 6), ('C++', 6), ('ООП', 5), ('React', 5), ('C#', 5), ('Английский язык', 5), ('MySQL', 4), ('Redux', 4), ('C/C++', 4), ('Django Framework', 3), ('RabbitMQ', 3), ('Kubernetes', 3), ('Обучение и развитие', 3), ('Bash', 3), ('ORACLE', 3), ('MS SQL', 3), ('Удаленная работа', 2), ('Qt', 2), ('.NET Framework', 2), ('CSS3', 2), ('HTML5', 2), ('ES6', 2), ('JS', 2), ('Аналитическое мышление', 2), ('Информационная безопасность', 2), ('Управление проектами', 2), ('PHP', 2), ('Golang', 2), ('Разработка ПО', 2), ('База данных: Oracle', 2), ('Oracle Pl/SQL', 2), ('ЦФТ', 2), ('ЦФТ-Банк', 2), ('АБС ЦФТ', 2), ('REST', 1), ('Flask', 1), ('Django', 1), ('WorldSkills', 1), ('Разработка нового продукта', 1), ('ELK', 1), ('Agile', 1), ('Elasticsearch', 1), ('SaaS', 1), ('APM', 1), ('Redis', 1), ('Celery + Flower', 1), ('Design Patterns', 1), ('MS Visual Studio', 1), ('Математический анализ', 1), ('Математическая статистика', 1), ('Биржевые торги', 1), ('PyCharm', 1), ('Творческое мышление', 1), ('Грамотная речь', 1), ('Работа в команде', 1), ('Ориентация на результат', 1), ('CMS Wordpress', 1), ('Преподаватель', 1), ('Обучение', 1), ('Zoom', 1), ('Умение общаться с людьми', 1), ('Желание зарабатывать', 1), ('Преподавание', 1), ('Индивидуальное обучение', 1), ('Репетитор', 1), ('Умение работать с детьми', 1), ('Педагог', 1), ('Образованность', 1), ('Scratch', 1), ('Unity', 1), ('Roblox Studio', 1), ('Minecraft Education Edition', 1), ('Atlassian Jira', 1), ('Atlassian Confluence', 1), ('TestRail', 1), ('Тестирование', 1), ('Функциональное тестирование', 1), ('Next.js', 1), ('GitLab', 1), ('React/Redux', 1), ('Разработка сайтов', 1), ('Бизнес-анализ', 1), ('Assembler', 1), ('Схемотехника электронного оборудования', 1), ('conan', 1), ('Linux kernel', 1), ('BPMN', 1), ('Оптимизация кода', 1), ('Написание инструкций', 1), ('Ansible', 1), ('Администрирование серверов Linux', 1), ('DevOps', 1), ('Turbo Pascal', 1), ('Линейное программирование', 1), ('Робототехника', 1), ('TIA Portal', 1), ('Лабораторная работа', 1), ('KUKA', 1), ('Autodesk Revit', 1), ('ArchiCAD', 1), ('AngularJS', 1), ('frontend', 1), ('Angular', 1), ('ARIS', 1), ('1с', 1), ('SSAS', 1), ('MS SQL Server', 1), ('SSRS', 1), ('ETL', 1), ('DWH', 1), ('Power BI', 1), ('OLAP', 1), ('Информационные технологии', 1), ('SIEM', 1), ('SOC', 1), ('Расследование инцидентов', 1), ('BDD', 1), ('QA', 1), ('Big Data', 1), ('Game Programming', 1), ('Team Lead', 1), ('Management', 1), ('Lead Programmer', 1), ('Lead Programming', 1), ('Gamedev', 1), ('Game Development', 1), ('Менеджмент', 1), ('Руководитель', 1), ('Ведущий разработчик', 1), ('Teamleading', 1), ('Управление командой', 1), ('B2C маркетинг', 1), ('Анализ бизнес показателей', 1), ('Руководство командой', 1), ('Управление персоналом', 1), ('Управление бизнес процессами', 1), ('опыт предпринимательства', 1), ('Selenium', 1), ('Product Management', 1), ('Business Development', 1), ('Team management', 1), ('Marketing Analysis', 1), ('Marketing Strategy Development', 1), ('Проектная документация', 1), ('Проектирование пользовательских интерфейсов', 1), ('Axure RP', 1), ('Figma', 1), ('Разработка технических заданий', 1), ('WebSphere', 1), ('IIS', 1), ('gRPC', 1), ('ElasticSearch', 1), ('CI/CD', 1), ('Boost', 1), ('jQuery', 1), ('руководство проектами', 1), ('проектный подход', 1), ('MongoDB', 1), ('TypeScript', 1), ('Ведение документации', 1), ('Kotlin', 1), ('Ajax', 1), ('Битрикс24', 1), ('Битрикс Управление сайтом', 1), ('1С-Битрикс', 1), ('CRM', 1)]
    # print(type(stat.get_stat()))
    # flash(stat.get_stat())
    # for i in posts:
    #     print(i[1], '  qwer  ', i[0])
    return render_template('results.html', title='Результаты', posts=stat.get_stat())


@app.route('/multiplication_table')
def multiplication_table():
    return render_template('multiplication_table.html', title='Multiplication table')

'''
[('Python', 34), ('Git', 14), ('Linux', 11), ('JavaScript', 11), ('SQL', 10), ('CSS', 9), ('PostgreSQL', 8), ('HTML', 8), ('Java', 7), ('Docker', 6), ('C++', 6), ('ООП', 5), ('React', 5), ('C#', 5), ('Английский язык', 5), ('MySQL', 4), ('Redux', 4), ('C/C++', 4), ('Django Framework', 3), ('RabbitMQ', 3), ('Kubernetes', 3), ('Обучение и развитие', 3), ('Bash', 3), ('ORACLE', 3), ('MS SQL', 3), ('Удаленная работа', 2), ('Qt', 2), ('.NET Framework', 2), ('CSS3', 2), ('HTML5', 2), ('ES6', 2), ('JS', 2), ('Аналитическое мышление', 2), ('Информационная безопасность', 2), ('Управление проектами', 2), ('PHP', 2), ('Golang', 2), ('Разработка ПО', 2), ('База данных: Oracle', 2), ('Oracle Pl/SQL', 2), ('ЦФТ', 2), ('ЦФТ-Банк', 2), ('АБС ЦФТ', 2), ('REST', 1), ('Flask', 1), ('Django', 1), ('WorldSkills', 1), ('Разработка нового продукта', 1), ('ELK', 1), ('Agile', 1), ('Elasticsearch', 1), ('SaaS', 1), ('APM', 1), ('Redis', 1), ('Celery + Flower', 1), ('Design Patterns', 1), ('MS Visual Studio', 1), ('Математический анализ', 1), ('Математическая статистика', 1), ('Биржевые торги', 1), ('PyCharm', 1), ('Творческое мышление', 1), ('Грамотная речь', 1), ('Работа в команде', 1), ('Ориентация на результат', 1), ('CMS Wordpress', 1), ('Преподаватель', 1), ('Обучение', 1), ('Zoom', 1), ('Умение общаться с людьми', 1), ('Желание зарабатывать', 1), ('Преподавание', 1), ('Индивидуальное обучение', 1), ('Репетитор', 1), ('Умение работать с детьми', 1), ('Педагог', 1), ('Образованность', 1), ('Scratch', 1), ('Unity', 1), ('Roblox Studio', 1), ('Minecraft Education Edition', 1), ('Atlassian Jira', 1), ('Atlassian Confluence', 1), ('TestRail', 1), ('Тестирование', 1), ('Функциональное тестирование', 1), ('Next.js', 1), ('GitLab', 1), ('React/Redux', 1), ('Разработка сайтов', 1), ('Бизнес-анализ', 1), ('Assembler', 1), ('Схемотехника электронного оборудования', 1), ('conan', 1), ('Linux kernel', 1), ('BPMN', 1), ('Оптимизация кода', 1), ('Написание инструкций', 1), ('Ansible', 1), ('Администрирование серверов Linux', 1), ('DevOps', 1), ('Turbo Pascal', 1), ('Линейное программирование', 1), ('Робототехника', 1), ('TIA Portal', 1), ('Лабораторная работа', 1), ('KUKA', 1), ('Autodesk Revit', 1), ('ArchiCAD', 1), ('AngularJS', 1), ('frontend', 1), ('Angular', 1), ('ARIS', 1), ('1с', 1), ('SSAS', 1), ('MS SQL Server', 1), ('SSRS', 1), ('ETL', 1), ('DWH', 1), ('Power BI', 1), ('OLAP', 1), ('Информационные технологии', 1), ('SIEM', 1), ('SOC', 1), ('Расследование инцидентов', 1), ('BDD', 1), ('QA', 1), ('Big Data', 1), ('Game Programming', 1), ('Team Lead', 1), ('Management', 1), ('Lead Programmer', 1), ('Lead Programming', 1), ('Gamedev', 1), ('Game Development', 1), ('Менеджмент', 1), ('Руководитель', 1), ('Ведущий разработчик', 1), ('Teamleading', 1), ('Управление командой', 1), ('B2C маркетинг', 1), ('Анализ бизнес показателей', 1), ('Руководство командой', 1), ('Управление персоналом', 1), ('Управление бизнес процессами', 1), ('опыт предпринимательства', 1), ('Selenium', 1), ('Product Management', 1), ('Business Development', 1), ('Team management', 1), ('Marketing Analysis', 1), ('Marketing Strategy Development', 1), ('Проектная документация', 1), ('Проектирование пользовательских интерфейсов', 1), ('Axure RP', 1), ('Figma', 1), ('Разработка технических заданий', 1), ('WebSphere', 1), ('IIS', 1), ('gRPC', 1), ('ElasticSearch', 1), ('CI/CD', 1), ('Boost', 1), ('jQuery', 1), ('руководство проектами', 1), ('проектный подход', 1), ('MongoDB', 1), ('TypeScript', 1), ('Ведение документации', 1), ('Kotlin', 1), ('Ajax', 1), ('Битрикс24', 1), ('Битрикс Управление сайтом', 1), ('1С-Битрикс', 1), ('CRM', 1)]
'''