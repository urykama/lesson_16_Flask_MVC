# Декларативное создание таблицы, класса и отображения за один раз
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///orm003.db', echo=True)
engine = create_engine('sqlite:///orm003.db', echo=False)

Base = declarative_base()


class Table_hh(Base):
    __tablename__ = 'Table_hh'
    id = Column(Integer, primary_key=True)
    requirement = Column(String(127))
    cnt = Column(Integer)

    # def __repr__(self):
    #     return self.requirement, self.cnt  # "'%s', '%s', '%s'" % (self.requirement, self.cnt, self.id)


# Создание таблицы
Base.metadata.create_all(engine)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()


def find(requirement):
    for item in requirement:
        fnd = session.query(Table_hh).filter(Table_hh.requirement == item['name']).first()
        if fnd is None:
            new_str = Table_hh(requirement=item['name'], cnt=1)
            session.add(new_str)
        else:
            fnd.cnt += 1
    session.commit()
    return 0


def get_stat_SQLite():
    return session.query(Table_hh).filter(Table_hh.cnt > 2).order_by(Table_hh.cnt.desc()).all()

# rq = session.query(Table_hh).filter(Table_hh.cnt > 7).order_by(Table_hh.cnt.desc()).all()
# # rq = session.query(Table_hh).all()
# print(type(rq), '\t', rq)
# for region in rq:
#     print(type(region), '\t', region.requirement)


# region = Region('Москва', 1)
# session.add(region)
#
# region = Region('Питер', 78)
# session.add(region)
#
# # session.rollback()  # Отмена
# session.commit()
# # изменение
# region.name = 'Тула'
# session.commit()
# # удаление
# session.delete(region)
# session.commit()

# for i in range(10):
#     region = Region(f'region {i}', 10 - i)
#     session.add(region)
# session.commit()

# выборка
# rq = session.query(Table_hh)  # Получаем объект запроса
# print("print(type(rq), rq)", '\t', type(rq), '\t', rq)
# for region in rq:
#     print(type(region), '\t', region)

# rq = session.query(Table_hh).all()
# print(type(rq), '\t', rq)
# for region in rq:
#     print(type(region), '\t', region)

# запрос с условием
# regions = session.query(Region).filter(Region.name == "Москва" and Region.id > 30).count()
# print(regions)

# regions = session.query(Table_hh).filter(Table_hh.requirement == "Python").count()
# print('print(regions)', '\t', regions)
#
# regions = session.query(Table_hh).count()
# print('print(regions)', '\t', regions)
#
# regions = session.query(Table_hh).group_by(Table_hh.requirement).count()
# print('print(regions)', '\t', type(regions), '\t', regions)
# print()
# regions = session.query(
#                             func.sum(Table_hh.id).label('id')
#                         ).group_by(Table_hh.requirement).subquery()
# print('print(regions)', '\t', type(regions), '\t', regions)


# regions = session.query(Table_hh).all()
# # regions = ['Git', 'Python', 'CSS']
# print('print(regions)', '\t', type(regions), '\t', regions)
# for i in regions:
#     if 'Git' == i.requirement:
#         print(123421541)
#         break
# print('Git' in regions.requirement)
# # for region in regions:
# #     print(type(region), '\t', region.requirement)
# regions = ['Git', 'Python', 'CSS']
# print('Git' in regions)
# print('print(regions)', '\t', type(regions), '\t', regions)

# regions = session.query(Table_hh).filter(Table_hh.requirement == "Flask456").first()
# print('print(regions)', '\t', regions)
# if regions is None:
#     print('count += 1')
# else:
#     print("regions.requirement = 'Flask456'")
# session.commit()

# last_cadre_movement = relation(
#     CadreMovement,
#     primaryjoin=and_(
#         CadreMovement.Table_hh == Table_hh.id,
#         uselist=False,
#         CadreMovement.id == select([func.max(CadreMovement.id)]).where(CadreMovement.Table_hh == Table_hh.id)
#     )
# )
