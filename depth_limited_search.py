# Функция поиска пути
# Поиск с ограничением глубины
# Возвращает кратчайший путь и список посещенных вершин в порядке обхода

def depth_limited_search(graph, start, goal, max_depth):
    # Проверка на валидность входных данных
    if start not in graph or goal not in graph:
        raise ValueError('Начальная или конечная вершина не найдена')

    # Стек вершин, которые необходимо обойти
    stack = [(start, 0)]
    # Словарь, где ключ - вершина, значение - родительская вершина
    parent = {start: None}
    # Список посещенных вершин
    visited = []

    while stack:
        # Последний элемент стека
        current, depth = stack.pop()
        visited.append(current)

        # Если текущая вершина является конечной, то поиск окончен
        if current == goal:
            break

        # Перебор смежных вершин
        for next in graph[current]:
            # Если смежная вершина еще не была посещена, то добавляем ее в стек
            if next not in parent and depth < max_depth:
                stack.append((next, depth + 1))
                parent[next] = current

    # Построение кратчайшего пути
    path = []
    current = goal
    while current:
        if current not in parent:
            return [], visited

        path.append(current)
        current = parent[current]

    return path[::-1], visited