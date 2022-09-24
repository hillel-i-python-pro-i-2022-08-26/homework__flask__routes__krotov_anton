from flask import Flask

import requests
import json
from faker import Faker

fake = Faker()


app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


@app.route("/requirements")
# '''
# Считывание файла
# PATH: /requirements/
# Возвращать содержимое файла. Любой текстовый файл.'''
def requirements():  # put application's code here
    text = open("/home/toxa/PycharmProjects/flaskProject/files/file.txt", "rt")
    return text.read()


@app.route("/generate-users")
# '''
# Сгенерировать данные пользователей и вывести на страницу.
# Формат данных: "Vasya example@mail.com"
# По умолчанию, пусть будет 100 пользователей. Добавить опциональный параметр,
# который регулирует количество пользователей.
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
    #    users = random.randint(0, 100)
    return (f"<p>{fake.first_name()} {fake.email()}</p>" for _ in range(100))


@app.route("/space")
def space():  # put application's code here
    space_req = requests.get("http://api.open-notify.org/astros.json")
    parse_req = json.loads(space_req.text)
    return str(parse_req["number"])


if __name__ == "__main__":
    app.run()
