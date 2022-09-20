from flask import Flask

import random

from faker import Faker
fake = Faker()


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/requirements')
# '''
# Считывание файла
# PATH: /requirements/
# Возвращать содержимое файла. Любой текстовый файл.'''
def requirements():  # put application's code here
    text = open("C:\\Users\\Toxa\\PycharmProjects\\flaskProject\\files\\file.txt", 'rt')
    return text.read()

@app.route('/generate-users')
# '''
# Сгенерировать данные пользователей и вывести на страницу.
# Формат данных: "Vasya example@mail.com"
# По умолчанию, пусть будет 100 пользователей. Добавить опциональный параметр, который регулирует количество пользователей.
# Библиотека в помощь: faker
#
# Примечание:
# ---
# В библиотеке есть в том числе возможность получить "просто имя". А не имя и фамилию.
# ---
# Разделите часть с генерацией данных и с форматированием их под вывод. Для этого может отлично подойти "генератор".
# ===
# '''
def generate_users():  # put application's code here
    return (f'<p>{fake.first_name()} {fake.first_name()}@mail.com</p>' for _ in range(100))

if __name__ == '__main__':
    app.run()
