import datetime

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()


class User(Base):
    """
    Описывает структуру таблицы athelete, содержащую данные об атлетах
    """
    __tablename__ = 'user'

    id = sa.Column(sa.Integer(), primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)

def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    print("Привет! Я запишу твои данные!")
    first_name = input("Введите своё имя:\n")
    last_name = input("А теперь фамилию:\n")
    gender = input("Укаэите свой пол (варианты: Male, Female)\n")
    email = input("Укажите адрес своей электронной почты:\n")    
    birthdate = input("Введи, пожалуйста, дату рождения в формате ГГГГ-ММ-ДД.\n ")
    height = input("Укажите свой рост в метрах, для отделения дробной части используйте точку")
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    return user

def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """

    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Ваши данные сохранены в базе")


if __name__ == "__main__":
    main()