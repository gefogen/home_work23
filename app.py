import os
from flask import Flask, redirect, request, abort

from classes import Request
from exceptions import NotValueError, NotTypeError, FailRequest
from settings import DATA_DIR

app = Flask(__name__)


@app.route("/perform_query/", methods=['GET', 'POST'])
def perform_query():
    try:
        cmd1 = request.args.get('cmd1')
        value1 = request.args.get('value1')
        cmd2 = request.args.get('cmd2')         # Получаем параметры запроса
        value2 = request.args.get('value2')
    except KeyError:
        raise FailRequest
    if not os.path.exists(DATA_DIR):
        return FailRequest

    try:
        with open(DATA_DIR, 'r') as file:
            first_result = getattr(Request, cmd1)(file, value1)     # getattr - возвращает значение атрибута объекта
            second_result = getattr(Request, cmd2)(first_result, value2)
    except (NotValueError, NotTypeError) as e:
        abort(400, e)

    return app.response_class(second_result, content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
