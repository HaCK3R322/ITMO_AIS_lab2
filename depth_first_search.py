# Функция поиска пути в целом
# Поиск в глубину
# Возвращает кратчайший путь и список посещенных вершин в порядке обхода

def depth_first_search(graph, start, end):
    # Проверка на валидность входных данных
    if start not in graph or end not in graph:
        raise ValueError('Начальная или конечная вершина не найдена')

    # Стек вершин, которые необходимо обойти
    stack = [start]
    # Словарь, где ключ - вершина, значение - родительская вершина
    parent = {start: None}
    # Список посещенных вершин
    visited = []

    while stack:
        # Последний элемент стека
        current = stack.pop()
        visited.append(current)

        # Если текущая вершина является конечной, то поиск окончен
        if current == end:
            break

        # Перебор смежных вершин
        for next in graph[current]:
            # Если смежная вершина еще не была посещена, то добавляем ее в стек
            if next not in parent:
                stack.append(next)
                parent[next] = current

    # Построение кратчайшего пути
    path = []
    current = end
    while current:
        path.append(current)
        current = parent[current]

    return path[::-1], visited