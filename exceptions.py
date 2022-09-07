class FailRequest(Exception):
    message = "Передано неверное имя файла"


class NotTypeError(Exception):
    message = "В функцию фильтра переданы неверные данные"


class NotValueError(Exception):
    message = "В функцию сортировки передан неверный аргумент"