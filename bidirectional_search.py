# Функция поиска пути
# Двунаправленный поиск в ширину
# Возвращает кратчайший путь и список посещенных вершин в порядке обхода

def bidirectional_search(graph, start, end):
    # Проверка на валидность входных данных
    if start not in graph or end not in graph:
        raise ValueError('Начальная или конечная вершина не найдена')

    # Очередь вершин, которые необходимо обойти
    queue_from_start = [start]
    queue_from_end = [end]
    # Словарь, где ключ - вершина, значение - родительская вершина
    parent_start = {start: None}
    parent_end = {end: None}
    # Список посещенных вершин
    visited = []

    common_vertex = None

    # find common vertex
    # then build path from start to common vertex and from common vertex to end

    while queue_from_start and queue_from_end:
        # Первый элемент очереди
        current_from_start = queue_from_start.pop(0)
        current_from_end = queue_from_end.pop(0)
        visited.append(current_from_start)
        visited.append(current_from_end)

        # Перебор смежных вершин
        for next in graph[current_from_start]:
            # Если смежная вершина еще не была посещена, то добавляем ее в очередь
            if next not in parent_start:
                queue_from_start.append(next)
                parent_start[next] = current_from_start
            if next in parent_end:
                common_vertex = next
                break
        for next in graph[current_from_end]:
            # Если смежная вершина еще не была посещена, то добавляем ее в очередь
            if next not in parent_end:
                queue_from_end.append(next)
                parent_end[next] = current_from_end
            if next in parent_start:
                common_vertex = next
                break

        if common_vertex:
            visited.append(common_vertex)
            break

    # build path from start to common vertex
    path_from_start = []
    current = common_vertex
    while current is not None:
        path_from_start.append(current)
        current = parent_start[current]

    # build path from common vertex to end
    path_from_end = []
    current = common_vertex
    while current is not None:
        path_from_end.append(current)
        current = parent_end[current]

    # reverse path from end
    path_from_end.reverse()
    path_from_start.reverse()

    # build path from start to end
    path = path_from_start + path_from_end

    return path, visited