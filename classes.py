from typing import Iterator, List, Iterable, Set, Union

from exceptions import NotTypeError, NotValueError


class Request:

    def filter(self: Iterator, string_to_search: str) -> Iterable:
        """Получить данные, которые содержат указанный текст"""
        if not isinstance(string_to_search, str):
            raise NotTypeError
        return filter(lambda line: string_to_search in line, self)

    def sort(self: Iterator, order: str = 'asc') -> List:
        """Сортировка данных в порядке возрастания или убывания"""
        if order not in ('asc', 'desc'):
            raise NotValueError
        if order == 'desc':
            return sorted(self, reverse=True)
        return sorted(self, reverse=False)

    def map(self: Iterator, column: Union[str, int]) -> Iterable:
        """Получить указанный столбец"""
        if not str(column).isdigit():
            raise NotTypeError
        return map(lambda line: line.split(' ')[int(column)] + '\n', self)

    def limit(self: Iterator, number: Union[str, int]) -> List:
        """Количество строк, возвращаемые переданным числом"""
        if not str(number).isdigit():
            raise NotTypeError
        return list(self)[:int(number)]

    def unique(self: Iterator, *args) -> Set:
        """Возвращать только уникальные строки"""
        return set(self)
