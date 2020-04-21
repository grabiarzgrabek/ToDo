# -*- coding: utf-8 -*-
# todo/todo.py

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Lista ToDo'


if __name__ == '__main__':
    app.run(debug=True)