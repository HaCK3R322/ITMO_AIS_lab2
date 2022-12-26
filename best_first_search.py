# best first search с учетом веса ребер

def best_first_search(graph, start, end):
    # Проверка на валидность входных данных
    if start not in graph or end not in graph:
        raise ValueError('Начальная или конечная вершина не найдена')

    # Список вершин, которые необходимо обойти
    queue = [(0, start)]
    # Словарь, где ключ - вершина, значение - родительская вершина
    parent = {start: None}
    # Список посещенных вершин
    visited = []
    # Словарь весов ребер
    weights = {}

    while queue:
        # Первый элемент очереди
        current = queue.pop(0)
        visited.append(current[1])

        # Если текущая вершина является конечной, то поиск окончен
        if current[1] == end:
            break

        # Перебор смежных вершин
        for next in graph[current[1]]:
            # Если смежная вершина еще не была посещена, то добавляем ее в очередь
            if next not in parent:
                # Вес ребра
                weight = graph[current[1]][next]
                queue.append((weight, next))
                parent[next] = current[1]
                weights[next] = weight

        # Сортировка очереди по весу ребра
        queue.sort(key=lambda x: x[0]['weight'])

    # Построение кратчайшего пути
    path = []
    current = end
    while current:
        path.append(current)
        current = parent[current]

    return path[::-1], visited