# Функция поиска пути
# Поиск в глубину с итеративным углублением
# Возвращает кратчайший путь и список посещенных вершин в порядке обхода
from depth_limited_search import depth_limited_search


def iterative_deeping_search(graph, start, end):
    # Проверка на валидность входных данных
    if start not in graph or end not in graph:
        raise ValueError('Начальная или конечная вершина не найдена')

    # Словарь, где ключ - вершина, значение - родительская вершина
    parent = {start: None}
    # Список посещенных вершин
    visited = []

    # Перебор глубин
    for depth in range(len(graph)):
        # Поиск в глубину с ограничением глубины
        path, visited = depth_limited_search(graph, start, end, depth)
        # Если путь найден, то поиск окончен
        if len(path) > 0:
            return path, visited, depth

    return [], visited, 0
